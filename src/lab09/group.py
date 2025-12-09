import csv
import datetime
from pathlib import Path
from collections import Counter
from src.lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()
        self._read_all()

    def _read_all(self):
        def fix_csv(row):
            row["gpa"] = float(row["gpa"])
            return row

        with self.path.open() as f:
            self.rows = [Student.from_dict(fix_csv(l)) for l in csv.DictReader(f)]

    def _ensure_storage_exists(self):
        if not self.path.exists():
            self.path.write_text("fio,birthdate,group,gpa\n", encoding="utf-8")

    def list(self):
        return self.rows

    def add(self, student: Student):
        self.rows.append(student)

    def find(self, substr: str):
        return [r for r in self.rows if substr in r.fio]

    def remove(self, fio: str):
        for i, r in enumerate(self.rows):
            if r.fio == fio:
                self.rows.pop(i)
                break

    def update(self, fio: str, **fields):
        stud = None
        for i, r in enumerate(self.rows):
            if r.fio == fio:
                stud = r
                break
        if not stud:
            raise ValueError("Student not found")

        for field, val in fields.items():
            match field:
                case "fio" | "group":
                    pass
                case "birthdate":
                    try:
                        datetime.date.fromisoformat(val)
                    except ValueError as e:
                        raise ValueError("birthdate format is be invalid") from e
                case "gpa":
                    if not (0 <= val <= 5):
                        raise ValueError("gpa must be between 0 and 5")
                case _:
                    raise ValueError("invalid Student field")

            setattr(stud, field, val)

    def stats(self) -> dict:
        sdict = {}

        sdict["count"] = len(self.rows)
        sdict["min_gpa"] = min(s.gpa for s in self.rows)
        sdict["max_gpa"] = max(s.gpa for s in self.rows)  # ловит даже в переходе Б-А
        sdict["avg_gpa"] = sum(s.gpa for s in self.rows) / len(self.rows)
        sdict["groups"] = dict(Counter(s.group for s in self.rows))
        sdict["top_5_students"] = [
            {"fio": s.fio, "gpa": s.gpa}
            for s in sorted(self.rows, key=lambda s: -s.gpa)[:5]
        ]

        return sdict
