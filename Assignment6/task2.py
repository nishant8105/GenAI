prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for price in prices:
    try:
        price = int(price)

        if price < 0:
            raise ValueError("Negative price not allowed")

        total += price

        print(f"Added {price}, Running total = {total}")

    except TypeError:
        print(f"TypeError: Invalid type skipped -> {price}")

    except ValueError as e:
        print(f"ValueError: {e} -> {price}")

print("Final Total:", total)