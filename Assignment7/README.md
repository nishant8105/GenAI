# Assignment 7

This assignment demonstrates Python object-oriented programming concepts such as classes, encapsulation, inheritance, abstraction, operator overloading, and polymorphism.

## Files and Topics

- `task1.py`
  - Defines a `Product` class with public attributes.
  - Shows how to print product details and apply a percentage discount.

- `task2.py`
  - Enhances `Product` with private price storage using `__price`.
  - Adds `get_price()` and `set_price()` methods for controlled access.
  - Demonstrates encapsulation and price validation.

- `task3.py`
  - Builds on `Product` and defines `ElectonicProduct` as a subclass.
  - Demonstrates inheritance and method overriding.
  - Adds a `warranty_year` attribute and customized `get_info()` output.

- `task4.py`
  - Defines `Laptop` and `Mobile` subclasses that extend `Product`.
  - Demonstrates polymorphism by storing both in a list and calling `get_info()`.

- `task5.py`
  - Implements an abstract `Payment` base class using `ABC`.
  - Adds concrete payment classes: `CreditCardPayment` and `UPIPayment`.
  - Demonstrates abstraction and interface implementation.

- `task6.py`
  - Extends `Product` with `__str__()` and `__add__()` operator overloading.
  - Shows printing product objects and adding two products by price.

- `task7.py`
  - Implements a simplified store inventory system with `Product`, `Inventory`, and `Store` classes.
  - Uses `__add__()` to combine product totals.
  - Demonstrates composition and basic interactive product management.

## How to run

Run each task with Python from the `Assignment7` directory:

```powershell
py task1.py
py task2.py
py task3.py
py task4.py
py task5.py
py task6.py
py task7.py
```

## Notes

- `task3.py` is imported by `task4.py`, so `task3.py` should remain present in the same folder.
- `task7.py` includes `input()` prompts for adding new products when `Store.add_new_product()` is used, but the current execution path only runs predefined sample data.
