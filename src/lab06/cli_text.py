import argparse


def main_cat(input_file: str, count: bool = False) -> None:
    """
    Выводит построчно указанный файл.

    input_file: Путь к файлу
    count: Выводить номера строка
    """
    with open(input_file) as f:
        for i, line in enumerate(f):
            print((f"{i+1:>4} " if count else "") + line)


def main_stats(input_file: str, top: int = 5) -> None:
    """
    Выводит статистику по файлу

    input_file: Путь к файлу
    top: Сколько слов выводить
    """
    with open(src) as f:
        doc = f.read()
    words = text.tokenize(text.normalize(doc))
    print(f"Всего слов: {len(words)}")
    freq = text.count_freq(words)
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top}:")
    top = text.top_n(freq, n=len(freq))
    tblprint.print_table(["слово", "частота"], top[:top])


def main():
    parser = argparse.ArgumentParser(
        prog="", description="CLI‑утилита для работы с файлами"
    )
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        main_cat(args.input, args.n)
    elif args.command == "stats":
        main_stats(args.input, args.top)


if __name__ == "__main__":
    main()
