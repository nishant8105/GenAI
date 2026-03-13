def apply_discount(price, discount_percentage = 5):
    if discount_percentage > 60 :
        return f"No discount {price}"
    return price - (price * discount_percentage) / 100

print(f"payable amount after discount {apply_discount(1000, 10)}")
print(f"payable amount after discount {apply_discount(500)}")
print(f"payable amount after discount {apply_discount(1000, 61)}")
