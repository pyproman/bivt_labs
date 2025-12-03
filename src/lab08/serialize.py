from .models import Student
import json


def students_to_json(students, path):
    data = [s.to_dict() for s in students]
    with open(path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path):
    with open(path) as f:
        return [Student.from_dict(i) for i in json.load(f)]
