history = []
memory = None

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else None

def main():
    global history, memory
    print("=== Simple Calculator ===")
    print("Available Operations: [A]dd (+) | [S]ubtract (-) | [M]ultiply (*) | [D]ivide (/)")

    use_smart_mode = True

    while True:
        if use_smart_mode:
            expr = input("🧮 Enter expression (e.g., 81 / 9): ").strip()
            try:
                if "mr" in expr.lower():
                    if memory is None:
                        raise ValueError("Memory is empty.")
                    expr = expr.lower().replace("mr", str(memory))
                # Basic sanitization: allow only digits, operators, decimal, parentheses
                if not all(c in "0123456789+-*/. ()" for c in expr):
                    raise ValueError("Invalid characters in expression.")
                result = eval(expr)
                history.append(f"{expr} = {result}")
                print(f"✅ Result: {result}")
            except Exception as e:
                print(f"❌ Error: {e}")
                continue

        mem_cmd = input("📌 [M+] Save | [MR] Recall | [MC] Clear | [H] History | Enter to skip: ").strip().lower()
        if mem_cmd == "m+":
            memory = result
            print("💾 Saved to memory.")
        elif mem_cmd == "mr":
            print(f"📥 Memory: {memory}")
        elif mem_cmd == "mc":
            memory = None
            print("🧹 Memory cleared.")
        elif mem_cmd == "h":
            print("🕘 History:")
            for item in history[-5:]:
                print("  -", item)

        again = input("🔁 Calculate again? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
