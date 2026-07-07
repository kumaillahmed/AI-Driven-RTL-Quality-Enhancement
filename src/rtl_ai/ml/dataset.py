import csv

def load_dataset(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))
