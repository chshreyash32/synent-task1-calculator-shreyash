"""
A simple CLI calculator that performs basic arithmetic operations.
Supports addition, subtraction, multiplication, and division with error handling.
"""

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract second number from first number."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide first number by second number.

    Args:
        x (float): Dividend
        y (float): Divisor

    Returns:
        float: Result of division

    Raises:
        ValueError: If attempting to divide by zero
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def get_number(prompt):
    """Get a valid number from user input.

    Args:
        prompt (str): Message to display to user

    Returns:
        float: Number entered by user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operation():
    """Get a valid operation from user input.

    Returns:
        str: Operation symbol (+, -, *, /)
    """
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        print("Invalid operation! Please enter +, -, *, or /.")

def calculate(num1, num2, operation):
    """Perform calculation based on operation.

    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation symbol

    Returns:
        float: Result of calculation

    Raises:
        ValueError: For invalid operations or division by zero
    """
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        raise ValueError(f"Unsupported operation: {operation}")

def main():
    """Main calculator loop."""
    print("=" * 40)
    print("          PYTHON CLI CALCULATOR")
    print("=" * 40)
    print("Supported operations: +, -, *, /")
    print("Type 'quit' or 'exit' to stop the calculator")
    print("-" * 40)

    while True:
        try:
            # Get first number
            num1_input = input("\nEnter first number (or 'quit' to exit): ").strip().lower()
            if num1_input in ['quit', 'exit']:
                print("Thank you for using the calculator! Goodbye!")
                break

            num1 = float(num1_input)

            # Get operation
            operation = get_operation()

            # Get second number
            num2 = get_number("Enter second number: ")

            # Perform calculation
            result = calculate(num1, num2, operation)

            # Display result
            print(f"\nResult: {num1} {operation} {num2} = {result}")

        except ValueError as e:
            if "could not convert string to float" in str(e):
                print("Invalid input! Please enter a valid number.")
            else:
                print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()