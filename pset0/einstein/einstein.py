def main():
    # Prompt user for mass
    m = get_int("m: ")

    # E = mc2
    # Energy = mass * squared (light speed) 300000000

    e = m * (300000000 ** 2)

    # Print energy
    print(e)


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()