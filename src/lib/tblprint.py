import os

def print_table(headers: list[str], data: list[list[str | int]]) -> None:
    """
    Печатает таблицу в консоль

    Поддерживает переменную окружения TABLE:
    - При TABLE=1 печатает через ASCII
    - При TABLE=FANCY печатает через Unicode и ANSI
    """
    column_length = [
        max(len(hdr), max(len(str(o[i])) for o in data)) if data else len(hdr)
        for i, hdr in enumerate(headers)
    ]
    match os.environ.get("TABLE", None):
        case "FANCY":
            print(
                "\x1b[42;30m" +
                " │ ".join(f"{hdr:<{column_length[i]}}" for i, hdr in enumerate(headers)) +
                "\x1b[0m"
            )
            for ri, row in enumerate(data):
                bg, fg = ((107,30),(100,37))[ri%2]
                print(
                    f"\x1b[{bg};{fg}m" +
                    f" \x1b[30m│\x1b[{fg}m ".join(f"{x:<{column_length[i]}}" for i, x in enumerate(row)) +
                    f"\x1b[0m")
        case None:
            for row in data:
                print(*row, sep=":")
        case _:
            print(
                " | ".join(f"{hdr:<{column_length[i]}}" for i, hdr in enumerate(headers))
            )
            print("-" * (sum(column_length) + 3 * len(headers) - 3))
            for row in data:
                print(" | ".join(f"{x:<{column_length[i]}}" for i, x in enumerate(row)))
