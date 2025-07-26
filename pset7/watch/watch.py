import re
import sys


def main():
    # Print new url
    print(parse(input("HTML: ")))


def parse(s):
    # Search for iframe tags
    if matches := re.search(r"^(<iframe.*<\/iframe>)$", s):
        for match in matches.groups():
            # Extract video part from url
            if url := re.search(r"https?:\/\/(?:www\.)?youtube\.com\/embed\/(\w+\d+)+", match):
                return "https://youtu.be/" + url.group(1)


if __name__ == "__main__":
    main()