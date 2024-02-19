r"""Finders
===========
"""

from dataclasses import dataclass

from lsprotocol.types import DiagnosticSeverity
from tree_sitter_lsp.finders import ErrorFinder, QueryFinder, SchemaFinder

from .schema import MuttTrie
from .utils import get_query, get_schema


@dataclass(init=False)
class ImportMuttFinder(QueryFinder):
    r"""Import mutt finder."""

    def __init__(
        self,
        message: str = "{{uni.get_text()}}: found",
        severity: DiagnosticSeverity = DiagnosticSeverity.Information,
    ):
        r"""Init.

        :param message:
        :type message: str
        :param severity:
        :type severity: DiagnosticSeverity
        """
        query = get_query("import")
        super().__init__(query, message, severity)


@dataclass(init=False)
class MuttFinder(SchemaFinder):
    r"""Muttfinder."""

    def __init__(self) -> None:
        r"""Init.

        :rtype: None
        """
        self.validator = self.schema2validator(get_schema())
        self.cls = MuttTrie


DIAGNOSTICS_FINDER_CLASSES = [
    ErrorFinder,
    MuttFinder,
]
