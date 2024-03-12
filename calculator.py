num1 = float(input("First Number: ").strip())
num2 = float(input("Second Number: ").strip())
op = input("Enter Operator (+, -, *, /): ").strip()

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")
