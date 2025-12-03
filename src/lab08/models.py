from dataclasses import dataclass
import datetime


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.date.fromisoformat(self.birthdate)
        except ValueError as e:
            raise ValueError("birthdate format is be invalid") from e

        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

    def age(self) -> int:
        b = datetime.date.fromisoformat(self.birthdate)
        today = datetime.date.today()
        return today.year - b.year - ((today.month, today.day) < (b.month, b.day))

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["fio"], d["birthdate"], d["group"], d["gpa"])

    def __str__(self):
        return f"{self.fio}, {self.group}, {self.gpa}"
