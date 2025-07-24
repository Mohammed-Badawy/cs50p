import random


def main():
    # Prompt for level
    level = get_level()

    # Count math problems
    math_problems = 0

    # Count total score
    score = 0

    while math_problems < 10:
        # Generate integers
        x = generate_integer(level)
        y = generate_integer(level)

        errors = 0
        prompt = f"{x} + {y} = "

        while True:
            try:
                # Prompt for answer
                answer = int(input(prompt))
            except ValueError:
                # Not valid types
                print("EEE")
                continue
            
            # Right answer
            if answer == (x + y):
                score += 1  # Count score
                break
            else:
                # Wrong answer
                print("EEE")

                # Wrong answer three times
                if errors == 2:
                    print(prompt, x + y)
                    error = 0
                    break
                errors += 1  # Count errors
                continue
        
        # Count math problems
        math_problems += 1
    # Print score
    print(f"Score: {score}")
        

def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level in [1, 2, 3]:
                return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)        


if __name__ == "__main__":
    main()
