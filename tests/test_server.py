import os

from mutt_language_server.server import MuttLanguageServer as Server

server = Server("")
file = os.path.join(os.path.dirname(__file__), "neomuttrc")


class Test:
    @staticmethod
    def test_check() -> None:
        diagnostics = server.lint(file)[file]
        assert len(diagnostics)

    @staticmethod
    def test_complete() -> None:
        contents = server.lookup("option", "sleep_time")["sleep_time"]
        assert len(contents)
