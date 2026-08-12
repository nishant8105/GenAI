# Python Functions and Functional Programming Assignment

This assignment contains Python scripts demonstrating the use of standard functions, recursion, lambda functions, and higher-order functions like `map()` and `filter()`.

## Files Overview

### `task1.py` - Standard Functions and Default Arguments
- **Functions:** Defines a function to calculate a discount, with a default discount parameter of 5%.
- Contains logic to cap the maximum discount at 60%.

### `task2.py` - Recursion and Exception Handling
- **Recursion:** Implements a recursive function to calculate the factorial of a given number.
- Raises and handles a `ValueError` if the input is a negative integer.

### `task3.py` - Lambda Functions
- **Lambda:** Defines simple lambda functions to calculate GST, discounts, and the final price by combining both operations.

### `task4.py` - The `map()` Function
- **Map:** Uses `map()` alongside a lambda function to apply an 18% GST to an entire list of prices, returning a new list.

### `task5.py` - The `filter()` Function
- **Filter:** Uses `filter()` to split a list of prices into two separate lists: one containing prices strictly greater than 500, and another for prices strictly less than 500.

### `task6.py` - Combining `map()` and `filter()`
- **Higher-Order Functions:** Defines a function that takes a list of prices, applies a 10% discount using `map()`, and extracts prices over 300 using `filter()`. Returns multiple values as a tuple.

### `task7.py` - Modular Application
- **Application:** Implements a menu-driven application to add prices to a list, calculate the average price, and find the maximum price using separate helper functions.
