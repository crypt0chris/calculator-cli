def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero"

def main():
    print("Simple Calculator")
    print("Options: add | subtract | multiply | divide")
    operation = input("Choose operation: ").strip().lower()
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if operation == "add":
        print("Result:", add(x, y))
    elif operation == "subtract":
        print("Result:", subtract(x, y))
    elif operation == "multiply":
        print("Result:", multiply(x, y))
    elif operation == "divide":
        print("Result:", divide(x, y))
    else:
        print("Unknown operation.")

if __name__ == "__main__":
    main()
