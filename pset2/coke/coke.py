def main():
    initial_amount = amount = 50
    total = 0

    # Get coins from user
    while amount > 0:
        print(f"Amount Due: {amount}")
        coins = get_int("Insert Coin: ")

        # Check coins in right denominations
        if coins not in [25, 10, 5]:
            continue

        amount -= coins
        total += coins

    # print owed coins
    print(f"Change Owed: {total - initial_amount}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()