# Python CLI Calculator

A simple command-line calculator built with Python that supports basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 🛡️ Error handling (invalid inputs, division by zero)
- 🔄 Continuous operation until user chooses to exit
- 🎯 Beginner-friendly code with clear comments
- 🧪 Includes unit tests

## Folder Structure

```
python_calculator/
├── src/
│   └── calculator.py          # Main calculator implementation
├── tests/
│   └── test_calculator.py     # Unit tests
├── docs/                      # Documentation (empty for now)
├── README.md                  # This file
└── requirements.txt           # Dependencies (none required beyond Python stdlib)
```

## How to Run

### Requirements
- Python 3.x (comes pre-installed on most systems)

### Running the Calculator

1. **Navigate to the project directory:**
   ```bash
   cd python_calculator
   ```

2. **Run the calculator:**
   ```bash
   python src/calculator.py
   ```

### Using in VS Code

1. Open VS Code
2. Open the `python_calculator` folder (`File > Open Folder`)
3. Make sure you have the Python extension installed (recommended)
4. Open `src/calculator.py`
5. Press `F5` or click the Run button to start debugging
6. Alternatively, open the terminal in VS Code (`Ctrl+` or `View > Terminal`) and run:
   ```bash
   python src/calculator.py
   ```

## How to Use the Calculator

When you run the calculator, you'll see:

```
========================================
          PYTHON CLI CALCULATOR
========================================
Supported operations: +, -, *, /
Type 'quit' or 'exit' to stop the calculator
----------------------------------------

Enter first number (or 'quit' to exit): 
```

Then:
1. Enter the first number
2. Choose an operation (+, -, *, /)
3. Enter the second number
4. See the result
5. Continue with another calculation or type 'quit' to exit

## Running Tests

To run the unit tests:

```bash
# From the project root directory
python -m unittest tests/test_calculator.py
```

Or to run with verbose output:
```bash
python -m unittest tests/test_calculator.py -v
```

## Example Usage

```
Enter first number (or 'quit' to exit): 10
Enter operation (+, -, *, /): *
Enter second number: 5

Result: 10.0 * 5.0 = 50.0

Enter first number (or 'quit' to exit): 15
Enter operation (+, -, *, /): /
Enter second number: 3

Result: 15.0 / 3.0 = 5.0

Enter first number (or 'quit' to exit): quit
Thank you for using the calculator! Goodbye!
```

## Error Handling

The calculator handles various error cases:
- Invalid number inputs (non-numeric values)
- Division by zero
- Invalid operation symbols
- Keyboard interrupts (Ctrl+C)

## Code Quality

The code follows Python best practices:
- Clear function documentation (docstrings)
- Meaningful variable names
- Proper error handling
- Separation of concerns (input, calculation, output)
- Beginner-friendly with explanatory comments

## 📸 Project Screenshots

### Calculator Output

(Screenshots/calculator-output.png)

### Another Example

(Screenshots/calculator-example.png)
## License

This project is open source and available for learning and modification.