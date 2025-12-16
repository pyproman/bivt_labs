from src.lab09.group import Group
from src.lab08.models import Student
from pathlib import Path


def test_load():
    grp = Group("data/lab09/students.csv")
    assert len(grp.list()) == 3


def test_add():
    grp = Group("data/lab09/students.csv")
    grp.add(Student("Сессиова Сессия Сессиавна", "2026-01-01", "СДАВ-АЙ-ТЕ", 5))
    found = False
    for i in grp.list():
        if i.fio == "Сессиова Сессия Сессиавна":
            found = True

    assert found


def test_find():
    grp = Group("data/lab09/students.csv")
    trump = grp.find("Джон")[0]
    assert str(trump) == "Дональд Джон Трамп, ДОГО-ВО-РНЯЧОК, 2.0"

    # меня pytest заставляет это делать
    assert trump.to_dict() == {
        "fio": "Дональд Джон Трамп",
        "birthdate": "1946-06-14",
        "group": "ДОГО-ВО-РНЯЧОК",
        "gpa": 2.0,
    }
    assert trump.age() > 78


def test_remove():
    grp = Group("data/lab09/students.csv")
    grp.remove("Дональд Джон Трамп")
    found = False
    for i in grp.list():
        if i.fio == "Дональд Джон Трамп":
            found = True

    assert not found


def test_update():
    grp = Group("data/lab09/students.csv")
    grp.update("Дональд Джон Трамп", gpa=3)  # договорнячок ближе
    assert grp.find("Джон")[0].gpa == 3


def test_update_checks():
    grp = Group("data/lab09/students.csv")
    grp.update(
        "Иванов Иван Иванович", gpa=4, birthdate="2038-01-19", group="ГДЕ-ТО-ТАМ"
    )

    try:
        grp.update("Иванов Иван Иванович", gpa=999)
        failed = False
    except ValueError:
        failed = True

    assert failed

    try:
        grp.update("Иванов Иван Иванович", birthdate="ИВАН-ИВ-АН")
        failed = False
    except ValueError:
        failed = True

    assert failed

    try:
        grp.update("Иванов Иван Иванович", group=" ")
        failed = False
    except ValueError:
        failed = True

    assert not failed

    try:
        grp.update("Иванов Иван Иванович", best=True)
        failed = False
    except ValueError:
        failed = True

    assert failed


def test_stats():
    grp = Group("data/lab09/students.csv")
    assert grp.stats() == {
        "count": 3,
        "min_gpa": 2.0,
        "max_gpa": 5.0,
        "avg_gpa": 11.5 / 3,
        "groups": {"БИВТ-25-2": 1, "УЧИТ-ЕЛ-И": 1, "ДОГО-ВО-РНЯЧОК": 1},
        "top_5_students": [
            {"fio": "Галина Сергеевна Крынецкая", "gpa": 5.0},
            {"fio": "Иванов Иван Иванович", "gpa": 4.5},
            {"fio": "Дональд Джон Трамп", "gpa": 2.0},
        ],
    }


def test_empty(tmp_path: Path):
    grp = Group(tmp_path / "empty.csv")
    try:
        grp.update("Илон Скам", gpa=3)
        found = True
    except ValueError:
        found = False

    assert not found


def test_stud_fields():
    # pytest заставил
    try:
        Student("Сессиова Сессия Сессиавна", "НЕ-СКАЖУ", "СДАВ-АЙ-ТЕ", 5)
        failed = False
    except ValueError:
        failed = True
    assert failed

    try:
        Student("Сессиова Сессия Сессиавна", "2026-01-01", "СДАВ-АЙ-ТЕ", 999)
        failed = False
    except ValueError:
        failed = True
    assert failed
