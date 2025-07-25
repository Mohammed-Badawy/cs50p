from csv import reader
from sys import argv, exit
from tabulate import tabulate


# Check command-line argument
if len(argv) < 2:
    exit("Too few command-line arguments")
elif len(argv) > 2:
    exit("Too many command-line arguments")

# Check file type
if not argv[1].endswith(".csv"):
    exit("Not a csv file")

rows = []

try:
    # Open and store data in rows
    with open(argv[1]) as file:
        read = reader(file)
        for row in read:
            rows.append(row)
except FileNotFoundError:
    exit("File doesn't exist")

# Print tabular data
print(tabulate(rows[1:], headers=rows[0], tablefmt="grid"))  