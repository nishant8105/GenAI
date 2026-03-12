order_list = []
while True:
    print("1 for add order")
    print("2 for all order and total")
    print("q for Quite")

    user_input = input("Enter input: ") 
    if user_input == "1":
        order_amount = int(input("Enter the order amount: "))
        order_list.append(order_amount)
    elif user_input == "2":
        for order in order_list:
            print(f"order amount is {order}", end = " ")
            revenue = 0
            for order in order_list:
                if order >= 2000:
                    final_amount = order - (order * 0.15)
                elif (order >= 1500) and (order < 2000):
                    final_amount = order - (order * 0.10)
                elif (order >= 1000) and (order < 1500) :
                    final_amount = order - (order * 0.07)

        Total += final_amount
        print("Total amount",Total)
    elif user_input == "q" :
        break

    else :
        continue