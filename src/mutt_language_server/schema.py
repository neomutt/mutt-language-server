r"""Schema
==========
"""

from dataclasses import dataclass

from lsp_tree_sitter import UNI
from lsp_tree_sitter.schema import Trie
from lsprotocol.types import Position, Range
from tree_sitter import Node

DIRECTIVES = {
    "set_directive",
    "source_directive",
}


@dataclass
class MuttTrie(Trie):
    r"""Mutt Trie."""

    value: dict[str, "Trie"] | list["Trie"] | str | int | bool | None

    @classmethod
    def from_node(cls, node: Node, parent: "Trie | None") -> "Trie":
        r"""From node.

        :param node:
        :type node: Node
        :param parent:
        :type parent: Trie | None
        :rtype: "Trie"
        """
        if node.type == "option":
            text = UNI.node2text(node)
            if text.startswith("no"):
                return cls(UNI.node2range(node), parent, "no")
            else:
                return cls(UNI.node2range(node), parent, "yes")
        if node.type == "int":
            return cls(UNI.node2range(node), parent, int(UNI.node2text(node)))
        if node.type == "\n":
            return cls(UNI.node2range(node), parent, "")
        if node.type in {"shell", "string", "quadoption"}:
            return cls(UNI.node2range(node), parent, UNI.node2text(node))
        if node.type == "file":
            trie = cls(Range(Position(0, 0), Position(1, 0)), parent, {})
            for child in node.children:
                if child.type not in DIRECTIVES:
                    continue
                # directive name
                _type = child.type.split("_directive")[0]
                # add directive name to trie.value if it doesn't exist
                _value: dict[str, Trie] = trie.value  # type: ignore
                if _type not in _value:
                    trie.value[_type] = cls(  # type: ignore
                        UNI.node2range(child),
                        trie,
                        {} if _type != "source" else [],
                    )
                # the dictionary's key corresponding to directive name
                subtrie: Trie = trie.value[_type]  # type: ignore
                # currently, only support set and source
                # set is a dict, source is a list
                value: dict[str, Trie] | list[Trie] = subtrie.value  # type: ignore
                # fill subtrie.value
                if child.type == "set_directive":
                    value: dict[str, Trie]
                    is_assign = False
                    for grandchild in child.children[1:]:
                        if grandchild.type == "=":
                            is_assign = True
                            break
                    # set option = value
                    if is_assign:
                        items = []
                        for grandchild in child.children[1:]:
                            if grandchild.type in {
                                " ",
                                "=",
                                "+=",
                                "-=",
                                '"',
                                "'",
                                "`",
                            }:
                                continue
                            items += [grandchild]
                        for k, v in zip(items[::2], items[1::2], strict=False):
                            value[UNI.node2text(k)] = cls.from_node(v, subtrie)
                    # set option nooption invoption & option ? option
                    else:
                        for grandchild in child.children[1:]:
                            if grandchild.type in {"&", "?", " "}:
                                continue
                            text = UNI.node2text(grandchild)
                            if text.startswith("no"):
                                # generate trie from option node
                                value[text.split("no")[-1]] = cls.from_node(
                                    grandchild, subtrie
                                )
                            elif text.startswith("inv"):
                                value[text.split("inv")[-1]] = cls.from_node(
                                    grandchild, subtrie
                                )
                            else:
                                value[text] = cls.from_node(
                                    grandchild, subtrie
                                )
                elif child.type == "source_directive":
                    value += [  # type: ignore
                        cls(
                            UNI.node2range(child.children[1]),
                            subtrie,
                            UNI.node2text(child.children[1]),
                        )
                    ]
            return trie
        raise NotImplementedError(node.type)
