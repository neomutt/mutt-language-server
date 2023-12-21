r"""Misc
========
"""
import re
from typing import Any

from tree_sitter_lsp.misc import get_md_tokens


def get_schema() -> dict[str, Any]:
    r"""Get schema.

    :rtype: dict[str, Any]
    """
    tokens = get_md_tokens("neomuttrc")
    indices = []
    end_index = len(tokens)
    for i, token in enumerate(tokens):
        if token.content == "PATTERNS":
            end_index = i
            break
        if (
            token.type == "code_block"
            and token.content.islower()
            or token.type == "inline"
            and token.content.startswith("**")
            and token.content.endswith("*")
        ):
            indices += [i]
    items = {}
    for i, index in enumerate(indices):
        keywords = [
            line.split()[0].strip("*")
            for line in tokens[index].content.splitlines()
        ]
        for keyword in keywords:
            items[keyword] = ""
        if len(indices) - 1 == i:
            index2 = end_index
        else:
            index2 = indices[i + 1]
        for token in tokens[index + 1 : index2]:
            if token.content != "" and not token.content.startswith("<!--"):
                for keyword in keywords:
                    items[keyword] += token.content
        for keyword in keywords:
            items[keyword] = tokens[index].content + re.sub(
                r"\n\s*", " ", items[keyword]
            )

    indices = []
    for i, token in enumerate(tokens[end_index:], end_index):
        if token.content == "SEE ALSO":
            end_index = i
            break
        if (
            token.type == "inline"
            and token.content.islower()
            and token.content.startswith("**")
            and token.content.endswith("**")
        ):
            indices += [i]
    for i, index in enumerate(indices):
        keyword = tokens[index].content.strip("*")
        items[keyword] = ""
        if len(indices) - 1 == i:
            index2 = end_index
        else:
            index2 = indices[i + 1]
        for token in tokens[index + 1 : index2]:
            if (
                token.content != ""
                and not token.content.startswith("<!--")
                and token.content != ":"
            ):
                if items[keyword] == "":
                    items[keyword] = token.content
                else:
                    items[keyword] += "\n" + re.sub(
                        r"\n\s*", " ", token.content
                    )

    return items
