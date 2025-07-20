from sys import exit
def main():
    # Prompt user
    dollars = to_float(input("How much was the meal? "), "$")
    percent = to_float(input("What percentage would you like to tip? "), "%") / 100

    # print tip
    print(f"Leave ${dollars * percent : .2f}")




def to_float(txt, symbol=" "):
    try:
        return float(txt.strip(symbol))
    except ValueError:
        print("Couldn't convert to float!")
        exit(1)


main()