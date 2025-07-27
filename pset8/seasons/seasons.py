from datetime import date
import inflect
from sys import exit


def main():
    # Prompt user for birthday date
    birthday = input("Date of Birth: ").strip()

    # Print number of minutes since this date
    print(convert_minutes(birthday))
    

# Convert date to minutes
def convert_minutes(d):
    # convert if valid or exit 
    try:
        minutes = (date.today() - date.fromisoformat(d)).days * 24 * 60
        p = inflect.engine()
        return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"
    except:
        exit("Invalid date")
    

if __name__ == "__main__":
    main()