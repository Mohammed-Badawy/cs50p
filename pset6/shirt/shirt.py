from PIL import Image, ImageOps
from sys import argv, exit


# Valid extensions
EXTENSIONS = ["jpeg", "jpg", "png"]

# Check command-line argument
if len(argv) < 3:
    exit("Too few command-line arguments")
elif len(argv) > 3:
    exit("Too many command-line arguments")

# Check files type
try:
    n1, ext1 = argv[1].lower().split(".")
    n2, ext2 = argv[2].lower().split(".")
except:
    exit("Invalid input")

# Check files extensions
if ext1 not in EXTENSIONS or ext2 not in EXTENSIONS or ext1 != ext2:
    exit("Invalid input")

try:
    # Open file
    img = Image.open(argv[1])
except FileNotFoundError:
    exit(f"Couldn't open {argv[1]}")

# Open shirt image and get it's size
shirt = Image.open("shirt.png")
size = shirt.size

# Fit image to shirt size
img = ImageOps.fit(img, size)
img.paste(shirt, shirt)

# Save image
img.save(argv[2])

