from ..lib.test import run
from ..lib import text

if __name__ == "__main__":
    run(lambda: text.normalize("ПрИвЕт\nМИр\t"), result="привет мир")
    run(lambda: text.normalize("ёжик, Ёлка"), result="ежик, елка")
    run(lambda: text.normalize("Hello\r\nWorld"), result="hello world")
    run(lambda: text.normalize("  двойные   пробелы  "), result="двойные пробелы")

    run(
        lambda: text.normalize("Ёлки\tиголки", casefold=False, yo2e=False),
        result="Ёлки иголки",
    )

    run(lambda: text.tokenize("привет мир"), result=["привет", "мир"])
    run(lambda: text.tokenize("hello,world!!!"), result=["hello", "world"])
    run(lambda: text.tokenize("по-настоящему круто"), result=["по-настоящему", "круто"])
    run(lambda: text.tokenize("2025 год"), result=["2025", "год"])

    run(lambda: text.tokenize("emoji 😀 не слово"), result=["emoji", "не", "слово"])

    r1 = {"a": 3, "b": 2, "c": 1}
    run(lambda: text.count_freq(["a", "b", "a", "c", "b", "a"]), result=r1)
    run(lambda: text.top_n(r1, n=2), result=[("a", 3), ("b", 2)])

    r2 = {"aa": 2, "bb": 2, "cc": 1}
    run(lambda: text.count_freq(["bb", "aa", "bb", "aa", "cc"]), result=r2)
    run(lambda: text.top_n(r2, n=2), result=[("aa", 2), ("bb", 2)])
