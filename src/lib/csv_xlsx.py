import csv
import xlsxwriter

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Преобразует CSV в XLSX
    Заголовок обязателен, значения сохраняются как строки.

    csv_path: Путь к CSV файлу
    xlsx_path: Путь к XLSX файлу
    """
    with open(csv_path) as f:
        ccon = list(csv.DictReader(f))

    workbook = xlsxwriter.Workbook(xlsx_path)
    sheet = workbook.add_worksheet()
    for i, row in enumerate(ccon):
        for j, val in enumerate(row.values()):
            sheet.write(i, j, val)
    sheet.autofit()
    workbook.close()
