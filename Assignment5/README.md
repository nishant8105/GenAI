# Python Modules and Packages Assignment

This assignment demonstrates how to organize Python code into custom modules and packages, and how to import and use them in a main script.

## Files Overview

### `math_utils.py` - Custom Math Module
- **Module:** A standalone python file containing simple mathematical functions like `add()`, `subtract()`, and `square()`.

### `string_utils.py` - Custom String Module
- **Module:** Contains string manipulation functions such as `capitalize_words()`, `reverse_string()`, and `word_count()`.

### `shop_package/` - Custom Python Package
- **Package:** A directory that acts as a package, containing multiple modules like `discount.py` and `billing.py` (imported in the main script).

### `main.py` - Importing Modules
- **Imports:** Acts as the entry point script. It imports functions from `math_utils` (using an alias `mu` and direct imports), `string_utils` (as `su`), and specific functions from `shop_package`.
- Demonstrates calling the imported functions with various arguments to verify they work together.
