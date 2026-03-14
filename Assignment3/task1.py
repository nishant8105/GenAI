def apply_discount(price, discount_percent = 5):
    if discount_percent > 60:
        print(f"Discount {discount_percent}% exceeds 60%. Capping it at 60%.")
        discount_percent = 60

    final_price = price - (price * discount_percent / 100)
    return final_price

print(f"payable amount after discount {apply_discount(1000, 10)}")
print(f"payable amount after discount {apply_discount(500)}")
print(f"payable amount after discount {apply_discount(1000, 61)}")
