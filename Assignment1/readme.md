# Python Data Structures Assignment

This assignment contains a series of Python scripts demonstrating the practical use of fundamental data structures: Lists, Tuples, Sets, and Dictionaries.

## Files Overview

### `task1.py` - Lists and Tuples
- **Lists:** Creates a list of products, accesses elements by index (including negative indexing), and adds new products using the `.append()` method.
- **Tuples:** Demonstrates how to handle immutable tuples. It shows a workaround to update a tuple by temporarily converting it into a list, modifying the value, and converting it back into a tuple.

### `task2.py` - Sets
- **Sets:** Converts a list with duplicate category names into a set to extract unique categories.
- Demonstrates adding new elements to a set using the `.add()` method.
- Shows how to check if an item exists within a set using the `in` operator.
- Calculates the total number of unique categories using the `len()` function.

### `task3.py` - Dictionaries
- **Dictionaries:** Creates a dictionary mapping product names to their prices.
- Shows how to insert new key-value pairs (new products) and update existing values.
- Uses a `try...except` block to safely remove an item (`.pop()`) from the dictionary without throwing unhandled `KeyError` exceptions.
- Calculates the average price of all the products using a `for` loop.
- Finds and prints the products with the maximum and minimum prices using the `max()` and `min()` functions with the `key=dict.get` parameter.

### `task4.py` - Complex Data Structures
- **List of Tuples to Dictionary:** Works with a catalog structured as a list of tuples (containing product name, price, and category).
- Iterates over the catalog to group and map categories to products by building a new dictionary (`category_to_products`).
