f = open('sales_date2.txt', 'r')
print("Read entire file")
print(f.read())
f.close()

print("-"*50)
f = open('sales_date2.txt', 'r')
print("Read first line")
print(f.readline())
f.close()

~print("-"*50)
f = open('sales_date2.txt', 'r')
print("Read all line using readlines")
line = [line.strip() for line in f.readlines()]
print(line)
f.close()