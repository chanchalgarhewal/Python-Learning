a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
operator = input("Enter an operator (+,-,*,/):")

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b == 0:
        result = "cannot be divided by zero"
    else:
        result = a / b
else:
    result = "Error: Invalid operator"

print("Result:", result)
