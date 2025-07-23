import emoji

# Prompt user for text
emoj = input("Input: ").strip()

# Print suitable emoji
print("Output:", emoji.emojize(emoj, language="alias"))