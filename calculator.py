def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Simple Calculator: Addition and Subtraction")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+ or -): ").strip()
    if operation == '+':
        print(f"Result: {add(num1, num2)}")
    elif operation == '-':
        print(f"Result: {subtract(num1, num2)}")
    else:
        print("Invalid operation. Please enter + or -.")

if __name__ == "__main__":
    main()
        print("Simple Calculator")
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero")
                return
            result = num1 / num2
        else:
            print("Invalid operation")
            return

        print(f"Result: {result}")
