def calculator():
    print("Simple Calculator")
    print("------------------")

    try:
        num1 = float(input("Enter the first number: "))
        op = input("Choose an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation.")
            return

        print(f"Result: {num1} {op} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
