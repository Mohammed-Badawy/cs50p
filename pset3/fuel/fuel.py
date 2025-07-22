from sys import exit

res = 0
# Prompt user for fraction x/y
while True:
    exp = input("Fraction: ").split("/")

    # convert to int
    try:
        numerator = int(exp[0])
        denom = int(exp[1])

        # check if negative numbers
        if numerator < 0 or denom < 0:
            continue
    except ValueError:
        continue

    # check divide by zero
    try:
        res = round(numerator / denom * 100)
        if res > 100:
            continue
    except ZeroDivisionError:
        continue

    # print result
    if res <= 1:
        print("E")
        break
    elif res >= 99:
        print("F")
        break
    else:
        print(f"{res}%")
        break