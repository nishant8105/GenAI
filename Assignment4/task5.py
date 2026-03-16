with open("product.txt", 'w') as file:
    for i in range(3):
        product_name = input("Enter product name: ") 
        product_price = input("Enter product price: ")
        file.write(f"{product_name} | {product_price}\n")

file = open("product.txt",'r' )
print("Name | Price")
print(file.read())

# Name | Price
# fish | 250
# chick | 450
# socks | 100