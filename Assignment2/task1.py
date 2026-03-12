order_amount = int(input("Enter the amount of order : "))
if order_amount >= 2000:
    order_amount -= (order_amount * 0.15)
    print(f"Your bill amount is {order_amount} + 5% tax total {order_amount + (order_amount * 0.05)}")
elif (order_amount >= 1500) and (order_amount < 2000):
    order_amount -= (order_amount * 0.10)
    print(f"Your bill amount is {order_amount} + 5% tax total {order_amount + (order_amount * 0.05)}")
elif (order_amount >= 1000) and (order_amount < 1500) :
    order_amount -= (order_amount * 0.07)
    print(f"Your bill amount is {order_amount} + 5% tax total {order_amount + (order_amount * 0.05)}")
else :
    print(f"Your bill amount is {order_amount} + 5% tax total {order_amount + (order_amount * 0.05)}")