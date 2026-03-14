def add_prices(prices_list, price):
    prices_list.append(price)
    
def get_average_price(prices_list):
    sum = 0
    for i in prices_list:
        sum += i
    avg = sum/len(prices_list)
    print(f"Average price {avg}")
    
def get_max_price(prices_list):
    maximum = max(prices_list)
    print(f"Maximum price {maximum}")
    
prices_list = []
while True :
    print("=" * 50)
    print("\n1 for add price")
    print("2 for Show average of price")
    print("3 for higest price")
    print("q to Quit")
    user_input = input("Enter your choice: ")

    if user_input == "1":
        price = float(input("\nEnter amount: "))
        add_prices(prices_list, price)
    elif user_input == "2":
        get_average_price(prices_list)
    elif user_input == "3":
        get_max_price(prices_list)
    elif user_input == "q":
        break
    else :
        print("Enter valid input")