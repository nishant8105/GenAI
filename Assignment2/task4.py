daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0
for day in daily:
    if day > 0:
        total_sales += day
        print(f"Total sale = {total_sales}")
    elif day == 0 :
        print("Today no sale")
        continue
    elif day < 0 :
        print("Currupeted data")
        break

print(f"Total sale of week= {total_sales}")