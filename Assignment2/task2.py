orders = [1200, 2500, 800, 1750, 3000]

revenue = 0
for order in orders:
    if order >= 2000:
        final_amount = order - (order * 0.15)
        print(f"{order} -> discount 15% -> {final_amount}")
    elif (order >= 1500) and (order < 2000):
        final_amount = order - (order * 0.10)
        print(f"{order} -> discount 10% -> {final_amount}")
    elif (order >= 1000) and (order < 1500) :
        final_amount = order - (order * 0.07)
        print(f"{order} -> discount 07% -> {final_amount}")
    else :
        print(f"{order}  -> discount 0% -> {final_amount}")

    revenue += final_amount

print(f"Total revenue : {revenue}")