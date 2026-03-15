sales = [1200, 450, 980, 1500, 3000]
f = open('sales_date.txt', 'w')
for sale in sales:
    f.write(f'{str(sale)}\n')
f.close()

f = open('sales_date.txt', 'r')
print(f.read())
f.close()

f = open('sales_date.txt', 'w')
f.write(', '.join(str(sale) for sale in sales))
f.close()

f = open('sales_date.txt', 'r')
print("Comma seperated data")
print(f.read())
f.close()