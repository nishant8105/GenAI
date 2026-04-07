# 📘 Python Exception Handling Tasks

This repository contains a collection of Python scripts (`task1.py` to `task5.py`) that demonstrate different use cases of **exception handling** and input validation in Python.

Each task focuses on handling specific types of errors and ensuring robust program execution.

---

## 📂 Files Overview

### 🔹 Task 1 – Division with Exception Handling
📄 `task1.py`  

Handles division between two user inputs with proper error handling.

**Features:**
- Accepts numerator and denominator from user
- Handles:
  - `ZeroDivisionError`
  - `ValueError`
- Ensures program completion using `finally`

📌 Example behavior:
- Prevents division by zero  
- Rejects non-integer inputs  

---

### 🔹 Task 2 – Price List Processing
📄 `task2.py`  

Processes a list of prices with mixed data types and invalid values.

**Features:**
- Converts values to integers
- Skips invalid entries
- Raises custom error for negative values
- Maintains a running total

**Handled Exceptions:**
- `TypeError`
- `ValueError`

---

### 🔹 Task 3 – Age Validation
📄 `task3.py`  

Validates user age input within a realistic range.

**Features:**
- Accepts age input
- Uses a custom validation function
- Raises error if age is outside 1–120

**Handled Exception:**
- `ValueError`

---

### 🔹 Task 4 – File Reading with Error Handling
📄 `task4.py`  

Reads and displays the first 3 lines of a file.

**Features:**
- Takes file name as input
- Reads file content safely
- Handles file-related errors

**Handled Exceptions:**
- `FileNotFoundError`
- `PermissionError`

---

### 🔹 Task 5 – Shopping Cart System
📄 `task5.py`  

Simulates a simple shopping cart with input validation.

**Features:**
- Accepts multiple price inputs
- Stops input on `'q'`
- Rejects negative and invalid values
- Calculates:
  - Total items
  - Total bill

**Handled Exception:**
- `ValueError`

---

## 🚀 How to Run

1. Make sure Python is installed (Python 3.x recommended)
2. Clone or download this repository
3. Run any task file:

```bash
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py