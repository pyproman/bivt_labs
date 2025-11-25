import pytest
from src.lib import text as textlib


@pytest.mark.parametrize(
    "text, options, result",
    [
        ("ПрИвЕт\nМИр\t", {}, "привет мир"),
        ("ёжик, Ёлка", {}, "ежик, елка"),
        ("Hello\r\nWorld", {}, "hello world"),
        ("  двойные   пробелы  ", {}, "двойные пробелы"),
        ("Ёлки\tиголки", {"casefold": False, "yo2e": False}, "Ёлки иголки"),
        ("", {}, ""),
    ],
)
def test_normalize(text, options, result):
    assert textlib.normalize(text, **options) == result


@pytest.mark.parametrize(
    "text, tokens",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("", []),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize(text, tokens):
    assert textlib.tokenize(text) == tokens


@pytest.mark.parametrize(
    "arr, counted",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
    ],
)
def test_freq(arr, counted):
    assert textlib.count_freq(arr) == counted


@pytest.mark.parametrize(
    "counted, leaders",
    [
        ({"a": 3, "b": 2, "c": 1}, [("a", 3), ("b", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, [("aa", 2), ("bb", 2)]),
    ],
)
def test_top_n(counted, leaders):
    assert textlib.top_n(counted, n=2) == leaders
