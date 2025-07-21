# Prompt user for variable name
var = input("camelCase: ")

snake_case = ""

# Convert camelCase to snake_case
for l in var:
    if l.isupper():
        snake_case += ("_" + l.lower())
    else:
        snake_case += l

print(f"snake_case: {snake_case}")