import re
import sys


def main():
    # Print number of um in text
    print(count(input("Text: ")))


def count(s):
    # Count number of um in text
    matches = re.findall(r"\b(\W*)?um\b(\W*)?", s, flags=re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()