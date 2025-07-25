from sys import argv, exit


# Check command-line argument
if len(argv) < 2:
    exit("Too few command-line arguments")
elif len(argv) > 2:
    exit("Too many command-line arguments")

# Check file type
if not argv[1].endswith(".py"):
    exit("Not a python file")

count = 0
try:
    with open(argv[1]) as file:
        for line in file:
            # check comment or whitespaces
            if line.strip().startswith("#") or line.isspace():
                continue
            count += 1

except FileNotFoundError:
    exit("File doesn't exist")

print(count)