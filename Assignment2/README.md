# Assignment 2

This repository contains Python scripts for various assignments and tasks related to calculating discounts, managing orders, and computing total sales.

## File Overview

### [task1.py](./task1.py)
**Objective:** Calculate the final bill amount for a single order with input validation.
- Takes the order amount as user input.
- Validates the input using a `try-except` block to ensure only numeric values are processed.
- Applies a discount based on the order amount:
  - 15% discount for orders >= 2000.
  - 10% discount for orders between 1500 and 1999.
  - 7% discount for orders between 1000 and 1499.
- Adds a 5% tax to the discounted final amount.
- Prints the calculated final bill amount.

### [task2.py](./task2.py)
**Objective:** Calculate the total revenue from a predefined list of orders.
- Iterates over a list of order amounts: `[1200, 2500, 800, 1750, 3000]`.
- Applies the same discount logic as `task1.py` individually to each order.
- Calculates and prints the discounted amount for each order (0% discount applied to amounts under 1000).
- Computes and prints the total revenue generated from the discounted orders (does not include tax).

### [task3.py](./task3.py)
**Objective:** Interactive order management system with tabular reporting.
- Provides an interactive console menu with the following options:
  - **1**: Add a new order amount to the order list.
  - **2**: View all current order amounts and calculate their total sum applying the standard discount brackets.
  - **q**: Quit the application.
- Option 2 displays a formatted table showing Order Amount, Discount %, After Discount, and With 5% Tax.
- Uses a `while` loop to continuously prompt the user until they choose to quit.

### [task4.py](./task4.py)
**Objective:** Calculate the total weekly sales while handling edge cases (zero values and corrupted data).
- Iterates through a given list of daily sales: `[200, 150, 0, 400, 50, -1, 300]`.
- Accumulates valid positive sales and prints the running total.
- Skips days with `0` sales (outputs "Today no sale").
- Immediately stops calculating and handles negative values (e.g., `-1`) by outputting a warning for corrupted data.
- Prints the final total valid sales computed before any corrupted data was encountered.
