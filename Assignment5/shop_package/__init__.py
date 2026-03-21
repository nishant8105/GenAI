from discount import apply_discount, flat_discount
from billing import calculate_total, apply_tax

print(f"applied discount on 5000 {apply_discount(5000, 25)}")
print(f"Flat discount on 250 {flat_discount(250)}")
totalprice = [250, 498, 670, 128, 3827]
print(f"Total price {calculate_total(totalprice)}")
print(f"Applied tax on 5000 {apply_tax(5000)}")