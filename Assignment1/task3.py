price_dict= {
    "Laptop" : 84999.34,
    "Headphones" : 1289.56, 
    "Keyboard" : 789, 
    "Mouse" : 299, 
    "Monitor" : 25499, 
    "Webcam" : 1299}
print(f"price of products {price_dict}")

price_dict["USB"] = 649.87 # new products
print(f"\nUSB is added to price_dict {price_dict}")

price_dict["Mouse"] = 399 #update price
print(f"\nprice of Mouse is Updated {price_dict}")

try :
    price_dict.pop("Mouse")
    print(f"\nremove mouse from price_dict {price_dict}")
except :
    print("\nProduct is not in price_dict")

# Average of products
sum = 0
for i in price_dict :
    sum += price_dict[i]

print(f"\nAverage of price of all Product {sum/(len(price_dict) + 1)}\n")

maximum = max(price_dict, key=price_dict.get)
minimum = min(price_dict, key=price_dict.get)
print(f"Maximun price of {maximum} is {price_dict[maximum]}")
print(f"Minimum price of {minimum} is {price_dict[minimum]}")