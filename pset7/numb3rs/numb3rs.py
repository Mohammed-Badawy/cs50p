import re
import sys


def main():
    # Print True if valid or False if invalid ip
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Search for ip pattern
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for match in matches.groups():
            # Check each octet if valid or invalid
            if not 0 <= int(match) <= 255 or re.search(r"^0+\d+$", match):
                return False  # Invalid
        return True  # Valid
    
    # Return invalid if not ip pattern
    return False


if __name__ == "__main__":
    main()