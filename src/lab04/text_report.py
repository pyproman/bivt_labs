import argparse
from ..lib import text
from ..lib import tblprint
from ..lib import file_lib


def main_multiple(
    srcs: list[str], pff: str | None, totalf: str | None, encoding: str | None = None
) -> None:
    """
    Выполняет анализ нескольких файлов.

    srcs: список путей к файлам
    pff: путь к per_file.txt
    totalf: путь к total.txt

    encoding: кодировка (по умолчанию UTF-8)
    """
    per_file = []
    total = {}
    for src in srcs:
        doc = file_lib.read_text(src, encoding=encoding or "utf-8")
        words = text.tokenize(text.normalize(doc))
        freq = text.count_freq(words)
        top = text.top_n(freq, n=len(freq))
        per_file.extend([src, *i] for i in top)
        for word, count in freq.items():
            total[word] = total.get(word, 0) + count

    if pff:
        file_lib.ensure_parent_dir(pff)
        file_lib.write_csv(per_file, pff, ["file", "word", "count"])

    if totalf:
        file_lib.ensure_parent_dir(totalf)
        top = text.top_n(total, n=len(total))
        file_lib.write_csv(top, totalf, ["word", "count"])


def main_single(src: str, tgt: str | None = None, encoding: str | None = None) -> None:
    """
    Выполняет анализ одного файла.

    src: путь к файлу
    tgt: путь к выводу (CSV)

    encoding: кодировка (по умолчанию UTF-8)
    """
    doc = file_lib.read_text(src, encoding=encoding or "utf-8")
    words = text.tokenize(text.normalize(doc))
    print(f"Всего слов: {len(words)}")
    freq = text.count_freq(words)
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    top = text.top_n(freq, n=len(freq))
    tblprint.print_table(["слово", "частота"], top[:5])
    if tgt:
        file_lib.ensure_parent_dir(tgt)
        file_lib.write_csv(top, tgt, ["word", "count"])


def main():
    parser = argparse.ArgumentParser(
        prog="Text Report", description="Считает статистику по словам"
    )
    parser.add_argument("-i", "--in", required=True, nargs="+")
    parser.add_argument("-o", "--out")
    parser.add_argument("-e", "--encoding")
    parser.add_argument("-p", "--per-file")
    parser.add_argument("-t", "--total")
    args = parser.parse_args()
    in_files = getattr(args, "in")
    if len(in_files) == 1:
        if args.per_file or args.total:
            raise ValueError("--per-file and --total require multiple files")
        main_single(in_files[0], args.out, encoding=args.encoding)
    else:
        if args.out:
            raise ValueError("--out is only for single files")
        main_multiple(in_files, args.per_file, args.total, encoding=args.encoding)


if __name__ == "__main__":
    main()
