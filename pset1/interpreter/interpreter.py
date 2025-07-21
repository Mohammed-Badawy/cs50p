from sys import exit

# Prompt for math expression
expression = input("Expression: ").strip().split()

# Convert digits to float
try:
    x = float(expression[0])
    y = float(expression[2])
except ValueError:
    print("Not digits!")
    exit(1)
# Operator
operator = expression[1]

match operator:
    case "+":  # Addition
        print(f"{x + y:.1f}")
    case "-":  # Subtraction
        print(f"{x - y:.1f}")
    case "*":  # Multiplication
        print(f"{x * y:.1f}")
    case "/":  # Division
        try:  # Check division by zero
            print(f"{x / y:.1f}")
        except ZeroDivisionError:
            print("Can't divide by zero!")
            exit(1)
    case _:  # Default
        print("Unknown math operator!")
        exit(2)
