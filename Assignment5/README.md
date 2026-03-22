# Assignment 5

This directory contains Python tasks focusing on modular programming, creating custom modules, and organizing code into packages.

## Overview of Modules and Packages

### `math_utils.py`
A simple utility module for mathematical operations. It includes:
- `add(a, b)`: Returns the sum of two numbers.
- `subtract(a, b)`: Returns the difference between two numbers.
- `square(n)`: Returns the square of a number.

### `string_utils.py`
A utility module for string manipulation. It includes:
- `capitalize_words(text)`: Converts the given text to uppercase.
- `reverse_string(text)`: Returns the reversed version of the given string.
- `word_count(text)`: Returns the length (character count) of the string.

### `shop_package`
A package containing modules related to shop billing and discounts.
#### `billing.py`
- `calculate_total(prices)`: Takes a list or tuple of prices and returns the sum.
- `apply_tax(amount)`: Calculates and returns the amount with an additional 5% tax.
#### `discount.py`
- `apply_discount(price, percent)`: Applies a percentage-based discount to the price.
- `flat_discount(price)`: Applies a flat discount of 50 to the price.

### `main.py`
The main execution script that imports and demonstrates the usage of the functions defined in `math_utils.py`, `string_utils.py`, and the `shop_package` modules.
