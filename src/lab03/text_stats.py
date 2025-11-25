# Читает 1 строку
from ..lib import text
from ..lib import tblprint

if __name__ == "__main__":
    line = input()
    words = text.tokenize(text.normalize(line))
    print(f"Всего слов: {len(words)}")
    freq = text.count_freq(words)
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    top5 = text.top_n(freq, n=5)
    tblprint.print_table(["слово", "частота"], top5)
