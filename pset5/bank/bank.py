def main():
    # Prompt user for greeting
    greet = input("Greeting: ").strip()

    # Print value
    print(f"${value(greet)}")


# Check greeting message
def value(greeting):
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    
    return 100


if __name__ == "__main__":
    main()