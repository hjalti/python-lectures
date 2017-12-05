import csv

with open('very_simple.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open('very_simple.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

