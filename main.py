def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else None

def main():
    print("=== Simple Calculator ===")
    print("Available Operations: Add | Subtract | Multiply | Divide")
    operation = input("Choose operation: ").strip().lower()

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")
        return

    result = None
    if operation == "add":
        result = add(x, y)
    elif operation == "subtract":
        result = subtract(x, y)
    elif operation == "multiply":
        result = multiply(x, y)
    elif operation == "divide":
        result = divide(x, y)
        if result is None:
            print("❌ Error: Division by zero.")
            return
    else:
        print("❌ Unknown operation.")
        return

    print(f"✅ Result: {result}")

if __name__ == "__main__":
    main()
