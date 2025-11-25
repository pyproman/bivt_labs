import csv
from pathlib import Path
from typing import Iterable, Sequence

# import text


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текст из файла по пути в указанной кодировке (например, encoding="cp1251")

    Может вызвать FileNotFoundError и UnicodeDecodeError
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """
    Записывает CSV по указанному пути

    Заголовки необязательны
    """
    p = Path(path)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


def ensure_parent_dir(path: str | Path) -> None:
    """
    Создаёт родительские директории, если их ещё нет.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)
