# Taqueria menu
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# Sum total of items
total = 0

while True:
    try:
        # Prompt for new item
        item = input("Item: ").strip().title()

        # Check if in menu and add to total if exists
        if item in menu:
            total += menu.get(item)
            print(f"Total: ${total:.2f}", sep="")

    # exit loop using ctrl-d
    except EOFError:
        print()
        break
    