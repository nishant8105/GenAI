# Python File I/O Assignment

This assignment covers reading from and writing to text files in Python, demonstrating different modes and techniques for handling file data.

## Files Overview

### `task1.py` - Writing and Reading Strings
- **File Writing:** Writes a list of sales integers to `sales_data.txt` by explicitly writing newlines or using `.join()`.
- **File Reading:** Reads and prints the entire file content using `.read()`.

### `task2.py` - Different Reading Methods
- **Reading Lines:** Demonstrates multiple ways to read a file: `.read()` for the entire content, `.readline()` for a single line, and `.readlines()` to read all lines into a list.
- Uses list comprehension to strip newline characters.

### `task3.py` - Appending to Files
- **File Append Mode:** Opens `sales_data.txt` in append mode (`'a'`) to add new sales data without overwriting the existing content.

### `task4.py` - File Data Processing
- **Data Analysis:** Reads numeric data from a file line-by-line and converts it into a list of integers.
- Calculates and prints total sales, highest sale, lowest sale, and the average sale manually using loops.

### `task5.py` - Using Context Managers (`with`)
- **Context Manager:** Uses the `with open(...)` statement to write product names and prices to `product.txt`, ensuring proper file closure automatically.

### `task6.py` - Checking File Existence
- **OS Module:** Uses `os.path.exists()` to check if a user-specified file exists before attempting to open and read it, preventing errors.

### `task7.py` - Formatting and Writing Dictionaries
- **Dictionaries to File:** Iterates over a dictionary of products and prices, calculates a 15% discount, and formats this into a table inside `discount_report.txt`.
- Appends the total count and average discounted price at the end.
