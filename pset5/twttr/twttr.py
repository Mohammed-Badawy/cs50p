def main():
    # Prompt user for text 
    text = input("Input: ")

    # Print shorten text
    print(f"Output: {shorten(text)}")


def shorten(word):
    nword = ""
    # Check if word contains vowels
    for letter in word:
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            continue
        nword += letter
        
    # Return shorten
    return nword


if __name__ == "__main__":
    main()