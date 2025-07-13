def calculate(a, b, op):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        elif op == '':
            return a ** b
        elif op == '%':
            return a % b
        else:
            return "Invalid Operator"
    except ZeroDivisionError:
        return "Cannot divide by zero!"

def advanced_calculator():
    print("Advanced Calculator: +, -, *, /, ** (power), % (modulus)")
    while True:
        try:
            a = float(input("Enter first number: "))
            op = input("Enter operator: ")
            b = float(input("Enter second number: "))
            result = calculate(a, b, op)
            print("Result:", result)

            choice = input("Do another calculation with result? (y/n): ").lower()
            while choice == 'y':
                op = input("Enter next operator: ")
                b = float(input("Enter next number: "))
                result = calculate(result, b, op)
                print("Result:", result)
                choice = input("Continue? (y/n): ").lower()

            again = input("Start new? (y/n): ")
            if again.lower() != 'y':
                break
        except ValueError:
            print("Invalid input!")

advanced_calculator()