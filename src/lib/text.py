import re
import collections

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует строку. По умолачнию приводит к нижнему регистру (casefold) и
    заменяет Ё на Е и е на ё (yo2e)
    """
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "е")
    return " ".join(text.split())

def tokenize(text: str) -> list[str]:
    """
    Разделяет текст на слова, удаляя лишние символы (эмодзи)
    """
    return re.findall(r'\w+(?:-\w+)*', text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Считает частоту слов
    """
    return dict(collections.Counter(tokens).items())

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Считает топ-N по убыванию частоты и алфавиту слова.
    """
    return sorted(map(tuple, freq.items()), key=lambda o:(-o[1],o[0]))[:n]
