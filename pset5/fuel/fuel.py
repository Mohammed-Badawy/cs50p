def main():
    # Prompt for expression
    exp = input("Fraction: ")

    # Convert to percentage
    percentage = convert(exp)

    # Print fuel level
    print(gauge(percentage))


# Convert fraction to int
def convert(fraction):
    try:
        num, demon = fraction.split("/")
        num = int(num)
        demon = int(demon)
    except:
        raise ValueError

    try:
        if num <= demon and 0 >= (num / demon) <= 1 and (num > 0 and demon > 0):
            return int(round(num / demon * 100))
    except:
        raise (ZeroDivisionError, ValueError)


# Get fuel level
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()