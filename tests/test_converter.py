from src.lib import json_csv  # csv_xlsx, file_lib

from pathlib import Path
import json, csv  # у препода python 4 с autoimport не переживайте

import pytest


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_csv.json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    with src.open("w", encoding="utf-8") as f:
        dw = csv.DictWriter(f, data[0].keys())
        dw.writeheader()
        dw.writerows(data)

    json_csv.csv_to_json(str(src), str(dst))

    rows = json.loads(dst.read_text(encoding="utf-8"))
    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_tuda_obratno(tmp_path: Path):
    src = tmp_path / "people.json"
    mid = tmp_path / "people.csv"
    dst = tmp_path / "people2.json"

    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    json_csv.json_to_csv(str(src), str(mid))
    json_csv.csv_to_json(str(mid), str(dst))

    rows = json.loads(dst.read_text(encoding="utf-8"))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())
