order_list = []
while True:
    print("\n1 for add order")
    print("2 for all orders and total")
    print("q for Quit")

    user_input = input("Enter input: ")

    if user_input == "1":
        order_amount = int(input("Enter the order amount: "))
        order_list.append(order_amount)
        print(f"Order of {order_amount} added successfully.")

    elif user_input == "2":
        if not order_list:
            print("No orders yet.")
            continue

        print("\n" + "=" * 50)
        print(f"{'Order':>10} | {'Discount':>10} | {'After Discount':>15} | {'With 5% Tax':>12}")
        print("-" * 50)

        total_revenue = 0

        for order_item in order_list:
            if order_item >= 2000:
                discount_pct = 15
                final_amount = order_item - (order_item * 0.15)
            elif order_item >= 1500:
                discount_pct = 10
                final_amount = order_item - (order_item * 0.10)
            elif order_item >= 1000:
                discount_pct = 7
                final_amount = order_item - (order_item * 0.07)
            else:
                discount_pct = 0
                final_amount = order_item

            tax_amount = final_amount + (final_amount * 0.05)
            total_revenue += final_amount

            print(f"{order_item:>10} | {discount_pct:>9}% | {final_amount:>15.2f} | {tax_amount:>12.2f}")

        print("=" * 50)
        print(f"{'Total Revenue (before tax):':>38} {total_revenue:>10.2f}")
        print(f"{'Total Revenue (with 5% tax):':>38} {total_revenue + (total_revenue * 0.05):>10.2f}")
        print("=" * 50)

    elif user_input == "q":
        break

    else:
        print("Invalid option, please try again.")
        continue