from sys import exit

START_BREAKFAST = 7
END_BREAKFAST = 8
START_LUNCH = 12
END_LUNCH = 13
START_DINNER = 18
END_DINNER = 19


def main():
    # Prompt user for time
    meal_time = input("What time is it? ").strip().lower()

    # Convert time to float
    fnum = convert(meal_time)

    # Check meal time
    if START_BREAKFAST <= fnum <= END_BREAKFAST:
        print("breakfast time")
    elif START_LUNCH <= fnum <= END_LUNCH:
        print("lunch time")
    elif START_DINNER <= fnum <= END_DINNER:
        print("dinner time")


# Convert time to float
def convert(time):
    # Check time format
    if time.endswith("a.m.") or time.endswith("p.m."):
        time, format = time.split()
    else:
        format = ""
    
    h, m = time.split(":")

    # Convert to float
    try:
        hour = float(h)
        minutes = float(m)
    except ValueError:
        print("Not digits!")
        exit(1)

    # Convert hour to proper format
    if format == "":
        hour = hour
    elif format == "p.m." and hour <= 12:
        hour += 12
    elif format == "a.m." and hour >= 12:
        hour -= 12

    minutes /= 60

    return (hour + minutes)


if __name__ == "__main__":
    main()