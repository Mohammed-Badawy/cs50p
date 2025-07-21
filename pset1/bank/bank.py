# Prompt user for greeting
greet = input("Greeting: ").strip().lower()

# Check greeting message
if greet.startswith("hello"):
    print("$0")
elif greet.startswith("h"):
    print("$20")
else:
    print("$100")