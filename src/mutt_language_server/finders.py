r"""Finders
===========
"""

import os
from dataclasses import dataclass

from lsprotocol.types import DiagnosticSeverity
from tree_sitter_lsp.finders import QueryFinder
from tree_sitter_muttrc import language


@dataclass(init=False)
class ImportMuttFinder(QueryFinder):
    r"""ImportMuttFinder."""

    def __init__(
        self,
        message: str = "{{uni.get_text()}}: error",
        severity: DiagnosticSeverity = DiagnosticSeverity.Information,
    ):
        r"""Init.

        :param message:
        :type message: str
        :param severity:
        :type severity: DiagnosticSeverity
        """
        with open(
            os.path.join(
                os.path.join(
                    os.path.join(os.path.dirname(__file__), "assets"),
                    "queries",
                ),
                "import.scm",
            )
        ) as f:
            text = f.read()
        query = language.query(text)
        super().__init__(query, message, severity)
