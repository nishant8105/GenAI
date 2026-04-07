cart = []
while True:
    price = input("Enter the price")
    if price.lower() == 'q':
        break
    try :
        price = float(price)
        if price < 0 :
            raise ValueError("Negative price")
        cart.append(price)
    except ValueError as e :
        print("Invaild input", e)

print(f"Total items {len(cart)}")
print("Total bill", sum(cart))
print(cart)