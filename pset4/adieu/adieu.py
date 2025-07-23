import inflect

# Intialize handle
p = inflect.engine()

# List of names
names = []

while True:
    try:
        # Add new name to names
        names.append(input("Name: ").strip().capitalize())
    except EOFError:
        # Print output & break out of loop
        print()
        print("Adieu, adieu, to", p.join(names))
        break