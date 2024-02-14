r"""Test utils."""

from mutt_language_server.utils import get_schema


class Test:
    r"""Test."""

    @staticmethod
    def test_get_schema() -> None:
        assert get_schema()["properties"].get("set")
