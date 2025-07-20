def main():
    # Prompt user for text
    text = input()

    # print text with emojis
    print(convert(text))


def convert(txt):
    t = txt.replace(":)", "🙂")
    t = t.replace(":(", "🙁")

    return t


main()