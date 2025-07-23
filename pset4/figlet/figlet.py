import pyfiglet
import random
import sys

# Initialize figlet handle
figlet = pyfiglet.Figlet()

# Get list of fonts
fonts = figlet.getFonts()

font = ""

# Command-line arguments length
ln = len(sys.argv)

# Check number of command-line arguments
if ln == 1:
    # Get random font
    font = figlet.setFont(font=random.choice(fonts))
elif ln == 2:
    # Exit program if missing command-line arguments
    sys.exit("missing command-line argument")
elif ln == 3:
    # Check second command-line within valid values
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid first command-line argument")

    # Use font specified by command-line
    font = figlet.setFont(font=sys.argv[2])

# Prompt user for text
text = input("Input: ").strip()

# Print figlet text
print(figlet.renderText(text))
