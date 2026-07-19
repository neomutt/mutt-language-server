r"""Server
==========
"""

import os

from lsp_tree_sitter.completer import (
    PathCompleter,
    SchemaCompleter,
    ValueCompleter,
)
from lsp_tree_sitter.linter import PathLinter, SchemaLinter
from lsp_tree_sitter.server import TreeSitterLanguageServer
from tree_sitter import Language, Parser
from tree_sitter_muttrc import language as get_language_ptr
from tree_sitter_muttrc import queries


class MuttLanguageServer(TreeSitterLanguageServer):
    def __init__(self, *args, **kwargs) -> None:
        parser = Parser()
        language = Language(get_language_ptr())
        parser.language = language

        assets_path = os.path.join(os.path.dirname(__file__), "assets")
        schema_file = os.path.join(assets_path, "json", "muttrc.json")
        code_file = os.path.join(assets_path, "jq", "main.jq")
        schema_completer = SchemaCompleter.from_files(schema_file, code_file)
        code_file = os.path.join(assets_path, "jq", "value.jq")
        value_completer = ValueCompleter.from_files(schema_file, code_file)
        path_completer = PathCompleter(
            "path",
            {
                "muttrc*": "muttrc",
                "**/muttrc*": "muttrc",
                "neomuttrc*": "muttrc",
                "**/neomuttrc*": "muttrc",
            },
        )
        path_linter = PathLinter.from_queries(language, queries)
        schema_linter = SchemaLinter.from_queries(
            language, queries, schema_file
        )

        super().__init__(
            parser,
            (schema_linter, path_linter),
            (schema_completer, value_completer, path_completer),
            *args,
            **kwargs,
        )
