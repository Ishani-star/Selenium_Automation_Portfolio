import csv

def read_csv(file_path):
    with open(file_path, newline="") as file:
        return list(csv.DictReader(file))