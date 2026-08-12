# Python Exception Handling Assignment

This assignment covers how to handle runtime errors gracefully in Python using `try`, `except`, `finally`, and raising custom exceptions.

## Files Overview

### `task1.py` - Basic Exception Handling
- **Division by Zero:** Prompts the user for two numbers and attempts division.
- Catches `ZeroDivisionError` if the denominator is zero and `ValueError` if the input is not a number. Uses a `finally` block to signal completion.

### `task2.py` - Iterative Error Handling
- **Data Cleaning:** Iterates through a list of mixed data types (integers, strings) and negative values.
- Uses `try...except` inside a loop to catch `TypeError` (for bad types) and explicitly raises a `ValueError` for negative prices, continuing the loop safely.

### `task3.py` - Raising Custom Exceptions
- **Validation:** Defines an age-checking function that explicitly raises a `ValueError` if the provided age is out of realistic bounds (1 to 120).

### `task4.py` - File Handling Exceptions
- **File Errors:** Attempts to open a user-provided file name.
- Catches `FileNotFoundError` if the file doesn't exist and `PermissionError` if the script lacks access rights.

### `task5.py` - Practical Cart Validation
- **Continuous Validation:** Implements a cart loop that takes price inputs.
- Validates the input as a float and raises an error for negative prices. Non-numeric or invalid inputs are caught without crashing the application.