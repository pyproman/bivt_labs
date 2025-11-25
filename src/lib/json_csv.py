import csv
import json


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.

    Кодировка UTF-8. Порядок колонок — как в первом объекте.

    json_path: Путь к JSON файлу
    csv_path: Путь к CSV файлу
    """
    with open(json_path) as f:
        jcon = json.load(f)
    headers = [i for i in jcon[0]]
    with open(csv_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writerow({i: i for i in headers})  # lol
        for obj in jcon:
            writer.writerow(obj)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.

    csv_path: Путь к CSV файлу
    json_path: Путь к JSON файлу
    """
    with open(csv_path) as f:
        ccon = list(csv.DictReader(f))
    with open(json_path, "w") as f:
        json.dump(ccon, f, ensure_ascii=False, indent=2)
