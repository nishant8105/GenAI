sales = [1200, 450, 980, 1500, 3000]
f = open('sales_date.txt', 'w')
for sale in sales:
    f.write(f'{str(sale)}\n')
f.close()

f = open('sales_date.txt', 'r')
print("Read entire file")
print(f.read())
f.close()

print("-"*50)
f = open('sales_date.txt', 'r')
print("Read first line")
print(f.readline())
f.close()

~print("-"*50)
f = open('sales_date.txt', 'r')
print("Read all line using readlines")
line = [line.strip() for line in f.readlines()]
print(line)
f.close()