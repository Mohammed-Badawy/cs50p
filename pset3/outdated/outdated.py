# Months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    # Prompt user for date
    date = input("Date: ").strip()

    # Try split day as sample 9/8/1636
    try:
        m, d, y = date.split("/")

        # Check valid month and day 
        if (int(m) > 12 or int(m) < 1) or (int(d) > 31 or int(d) < 1):
            continue
        
        # Print new formatted date
        print(f"{y.zfill(4)}-{str(m).zfill(2)}-{str(d).zfill(2)}")
        break

    except ValueError:
        # Try split date with , as sample September 8, 1636
        try:
            date, y = date.split(",")
            m, d = date.split()
        except ValueError:
            continue
    
    # Check if month is alphabetical chars 
    if m.isalpha():
        m = months.index(m.capitalize())

        # Check valid day and month
        if (int(m) > 12 or int(m) < 1) or (int(d) > 31 or int(d) < 1):
            continue
        
        # Print new formatted date
        print(f"{y.zfill(4)}-{str(m + 1).zfill(2)}-{str(d).zfill(2)}")
        break