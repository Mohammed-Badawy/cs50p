import re
import sys


def main():
    # Print new time format
    print(convert(input("Hours: ")))


def convert(s):
    # Check time format and get matches or raise ValueError
    if matches := re.search(r"^((?:\d\d?):?(?:\d\d?)? (?:AM|PM)) to ((?:\d\d?):?(?:\d\d?)? (?:AM|PM))$", s):
        # Split time
        frm = matches.group(1)
        to = matches.group(2)
        fhour, fminutes, fformat = split_time(frm)
        thour, tminutes, tformat = split_time(to)
        
        # Return new format
        return f"{convert_format(fhour, fminutes, fformat)} to {convert_format(thour, tminutes, tformat)}"
    else:
        raise ValueError("Invalid time format")


# Split time into a tuple (hour, minutes, format)
def split_time(t):
    if matches := re.search(r"^(\d+):?(\d+)? (AM|PM)$", t):
        hour = int(matches.group(1))
        # if minutes is none then minutes = 0
        try:
            minutes = int(matches.group(2))
        except:
            minutes = 0

        format = matches.group(3)

        # Check valid format or raise ValueError
        if (hour > 12 and format == "PM") or 0 < minutes > 59 or hour > 12:
            raise ValueError
        
        return (hour, minutes, format)


# Convert to new format
def convert_format(h, m, f):
    if f == "AM":
        if h == 12:
            h = 0
        
        h = str(h).zfill(2)
        m = str(m).zfill(2)

        return f"{h}:{m}"

    elif f == "PM":
        if h == 12:
            h = 12
        else:
            h += 12
        
        h = str(h).zfill(2)
        m = str(m).zfill(2)
        return f"{h}:{m}"


if __name__ == "__main__":
    main()