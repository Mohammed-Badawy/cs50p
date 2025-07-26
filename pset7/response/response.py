from validator_collection import validators, errors

# Prompt user for email
email = input("What's your email address? ").strip()

try:
    # If valid print valid
    if validators.email(email):
        print("Valid")
# Raise InvalidEmailError
except errors.InvalidEmailError:
    print("Invalid")