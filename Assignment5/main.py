import math_utils as mu
from math_utils import square

print(f"Addition of 5 and 6 is {mu.add(5, 6)}")
print(f"subtraction of 18 and 3 is {mu.subtract(18, 3)}")
print(f"Square of 9 is {square(9)}")
print()
print("="*25)
import string_utils as su
print()
print(f"Capitalize word of 'nishant' is {su.capitalize_words('nishant')}")
print(f"Reverse of 'nishant' is {su.reverse_string('nishant')}")
print(f"Words count in 'nishant' is {su.word_count('nishant')}")

print()
print("="*25)
print()

import shop_package.discount as disc
from shop_package.billing import calculate_total

print(disc.apply_discount(1000, 10))
print(calculate_total([100, 200, 300]))