file = open("sales_data.txt", 'r')
lines = file.readlines()
sales = [int(line.strip()) for line in lines if line.strip()]
print("typr of sale[0]:",type(sales[0]))

total = sum(sales)
print("Total Sales  :", total)

maximum = sales[0]
for sale in sales :
    if maximum < sale :
        maximum = sale

print("Highest Sale : ", maximum)

minimum = sales[0]
for sale in sales :
    if minimum > sale :
        minimum = sale

print("Lowest Sale : ", minimum)

avg = total/len(sales)
print("Average sale :", avg)