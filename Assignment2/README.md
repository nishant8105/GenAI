# Python Control Flow and Loops Assignment

This assignment contains a series of Python scripts demonstrating the practical use of conditional statements, loops, and user input handling.

## Files Overview

### `task1.py` - Conditional Statements (if-elif-else)
- **Conditionals:** Takes an order amount as input and applies tiered discounts based on the amount.
- Calculates and prints the final bill amount including a 5% tax.
- Uses `try...except` block to handle invalid inputs (non-integer values).

### `task2.py` - For Loops and Conditionals
- **Loops:** Iterates through a predefined list of order amounts.
- Applies the same tiered discount logic (15%, 10%, 7%) using `if-elif-else` statements.
- Keeps track of the total revenue accumulated from all discounted orders.

### `task3.py` - While Loops and Menu System
- **Menu System:** Implements an interactive loop using `while True:` where a user can add orders or view a summary.
- **Order Management:** Appends new orders to a list and formats an output table showing the order, discount percentage, and final amount including a 5% tax.
- Calculates and displays the grand total revenue.

### `task4.py` - Loop Control Statements (continue and break)
- **Data Validation:** Iterates over a list of daily sales figures containing zero and negative values.
- Uses `continue` to skip over zero-value days without stopping the loop.
- Uses `break` to terminate the loop entirely if corrupted (negative) data is encountered.
