r"""Server
==========
"""
import os
import re
from typing import Any

from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    TEXT_DOCUMENT_DOCUMENT_LINK,
    TEXT_DOCUMENT_HOVER,
    CompletionItem,
    CompletionItemKind,
    CompletionList,
    CompletionParams,
    DocumentLink,
    DocumentLinkParams,
    Hover,
    MarkupContent,
    MarkupKind,
    Position,
    Range,
    TextDocumentPositionParams,
)
from pygls.server import LanguageServer

from .utils import get_schema

PAT = re.compile(r"(?<=\bsource\b\s)\S+")


class MuttLanguageServer(LanguageServer):
    r"""Mutt language server."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        r"""Init.

        :param args:
        :type args: Any
        :param kwargs:
        :type kwargs: Any
        :rtype: None
        """
        super().__init__(*args, **kwargs)

        @self.feature(TEXT_DOCUMENT_DOCUMENT_LINK)
        def document_link(params: DocumentLinkParams) -> list[DocumentLink]:
            r"""Get document links.

            :param params:
            :type params: DocumentLinkParams
            :rtype: list[DocumentLink]
            """
            document = self.workspace.get_document(params.text_document.uri)
            links = []
            for i, line in enumerate(document.source.splitlines()):
                for m in PAT.finditer(line):
                    _range = Range(
                        Position(i, m.start()), Position(i, m.end())
                    )
                    url = os.path.join(
                        os.path.dirname(params.text_document.uri),
                        os.path.expanduser(line[m.start() : m.end()]),
                    )
                    links += [DocumentLink(_range, url)]
            return links

        @self.feature(TEXT_DOCUMENT_HOVER)
        def hover(params: TextDocumentPositionParams) -> Hover | None:
            r"""Hover.

            :param params:
            :type params: TextDocumentPositionParams
            :rtype: Hover | None
            """
            word, _range = self._cursor_word(
                params.text_document.uri, params.position, True
            )
            properties = get_schema().get("properties", {})
            if _range.start.character != 0:
                properties = properties.get("set", {}).get("properties", {})
            description = properties.get(word, {}).get("description", {})
            if not description:
                return None
            return Hover(
                MarkupContent(MarkupKind.Markdown, description), _range
            )

        @self.feature(TEXT_DOCUMENT_COMPLETION)
        def completions(params: CompletionParams) -> CompletionList:
            r"""Completions.

            :param params:
            :type params: CompletionParams
            :rtype: CompletionList
            """
            word, _range = self._cursor_word(
                params.text_document.uri, params.position, False
            )
            properties = get_schema().get("properties", {})
            if _range.start.character != 0:
                properties = properties.get("set", {}).get("properties", {})
            items = [
                CompletionItem(
                    x,
                    kind=(
                        CompletionItemKind.Constant
                        if property.get("description", "").startswith("Type:")
                        else CompletionItemKind.Function
                    ),
                    documentation=MarkupContent(
                        MarkupKind.Markdown, property.get("description", "")
                    ),
                    insert_text=x,
                )
                for x, property in properties.items()
                if x.startswith(word)
            ]
            return CompletionList(False, items)

    def _cursor_line(self, uri: str, position: Position) -> str:
        r"""Cursor line.

        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :rtype: str
        """
        document = self.workspace.get_document(uri)
        return document.source.splitlines()[position.line]

    def _cursor_word(
        self,
        uri: str,
        position: Position,
        include_all: bool = True,
        regex: str = r"\w+",
    ) -> tuple[str, Range]:
        """Cursor word.

        :param self:
        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :param include_all:
        :type include_all: bool
        :param regex:
        :type regex: str
        :rtype: tuple[str, Range]
        """
        line = self._cursor_line(uri, position)
        for m in re.finditer(regex, line):
            if m.start() <= position.character <= m.end():
                end = m.end() if include_all else position.character
                return (
                    line[m.start() : end],
                    Range(
                        Position(position.line, m.start()),
                        Position(position.line, end),
                    ),
                )
        return (
            "",
            Range(Position(position.line, 0), Position(position.line, 0)),
        )
