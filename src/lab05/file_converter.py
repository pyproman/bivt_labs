from ..lib import json_csv, csv_xlsx, file_lib

file_lib.ensure_parent_dir("data/out/people.csv")
json_csv.json_to_csv("data/samples/people.json", "data/out/people.csv")
json_csv.csv_to_json("data/samples/people.csv", "data/out/people.json")
csv_xlsx.csv_to_xlsx("data/samples/cities.csv", "data/out/people.xlsx")

json_csv.json_to_csv("data/samples/ports.json", "data/out/ports.csv")
json_csv.csv_to_json("data/samples/ports.csv", "data/out/ports.json")
csv_xlsx.csv_to_xlsx("data/samples/labs.csv", "data/out/labs.xlsx")
