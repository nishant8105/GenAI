prices = {
    "Mouse   ": 500,
    "Keyboard": 800,
    "Moniter ": 7000,
    "Pendrive": 400,
    "Camera  ": 5000
}
file = open("discount_report.txt", 'w')
file.write("key      | value | 15% discount \n")
sum = 0
for key, value in prices.items():
    file.write(f"{key} | {value}   | {value - (value * 0.15)}\n")
    sum += value
file.close()

with open("discount_report.txt","r") as file:
    print(file.read())
with open("discount_report.txt","a") as file:
    file.write(f"Total Items : {sum}\n")
    avg = sum/len(prices)
    file.write(f"Average Discountes Price : {avg}\n")
