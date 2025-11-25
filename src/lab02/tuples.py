from ..lib.test import run


def format_record(rec: tuple[str, str, float]) -> str:
    """
    Возвращает строку из записи (fio: str, group: str, gpa: float).
    Пример: Иванов И.И., гр. BIVT-25, GPA 4.60
    """
    initials = rec[0].split()
    if len(initials) not in (2, 3):
        raise ValueError("Unsupported initials length")
    fmti = f"{initials[0].title()} {initials[1][0].upper()}."
    if len(initials) == 3:
        fmti += f"{initials[2][0].upper()}."
    return f"{fmti}, гр. {rec[1].strip()}, GPA {rec[2]:.2f}"


if __name__ == "__main__":
    run(
        lambda: format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)),
        result="Иванов И.И., гр. BIVT-25, GPA 4.60",
    )
    run(
        lambda: format_record(("Петров Пётр", "IKBO-12", 5.0)),
        result="Петров П., гр. IKBO-12, GPA 5.00",
    )
    run(
        lambda: format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)),
        result="Петров П.П., гр. IKBO-12, GPA 5.00",
    )
    run(
        lambda: format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)),
        result="Сидорова А.С., гр. ABB-01, GPA 4.00",
    )
