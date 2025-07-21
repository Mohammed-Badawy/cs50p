# Prompt user for text
text = input("Input: ")

new_version = ""

for l in text:
    if l.lower() in ["a", "e", "i", "o", "u"]:
        continue
    
    new_version += l

# Print new version
print(f"Output: {new_version}")