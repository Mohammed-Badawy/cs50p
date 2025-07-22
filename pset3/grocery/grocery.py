# Store grocery items
items = {}

while True:
    try:
        # Prompt for new item
        item = input().upper()

        # Add or update item in items
        items[item] = items.get(item, 0) + 1

    # Exit loop using ctrl-d
    except EOFError:
        print()
        break

# Print sorted items
for item in sorted(items):
    print(f"{items[item]} {item}")