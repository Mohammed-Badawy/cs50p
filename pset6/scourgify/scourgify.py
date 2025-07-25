import csv
from sys import argv, exit


# Check command-line argument
if len(argv) < 3:
    exit("Too few command-line arguments")
elif len(argv) > 3:
    exit("Too many command-line arguments")

persons = []

try:
    # Open and store data in rows
    with open(argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            tmp = {}
            # Split name and store data in tmp dictionary
            last, first = row["name"].split(", ")
            tmp["first"] = first
            tmp["last"] = last
            tmp["house"] = row["house"]
            persons.append(tmp)
except FileNotFoundError:
    exit(f"Couldn't read {argv[1]}")

# Open output file for writing
with open(argv[2], "w") as output:
    # Write fieldnames
    fields = ["first", "last", "house"]
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()

    # Write persons info
    for p in persons:
        writer.writerow(p)