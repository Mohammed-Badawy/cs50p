def main():
    plate = input("Plate: ").upper()
    
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check first two chars must be letters
    if not s[:2].isalpha():
        return False

    # Check length
    ln = len(s)

    if ln < 2 or ln > 6:
        return False
    
    is_fdigit = False

    for c in s:
        # Get first digit
        if c.isdigit():
            # Check first digit mustn't be 0
            if c == '0' and not is_fdigit:
                return False
            
            is_fdigit = True
        
        # Check contains any alpha after digits and any alnum char
        if (is_fdigit and c.isalpha()) or not c.isalnum():
            return False
    
    return True


main()