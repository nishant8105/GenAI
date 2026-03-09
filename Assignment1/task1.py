products = ["Laptop", "Headphones", "Keyboard", "Mouse", "Monitor", "Webcam"]
sample_prodcut = ("Laptop", 12999, "Electronics")

# print 2nd and last product from list
print("2nd product",prodcuts[1])
print("last product", prodcuts[-1])

# append 2 prodcuts
prodcuts.append("USB Hub")
prodcuts.append("Desk Lamp")

# print updated list
print("Updated list", prodcuts)

# optional
sample_prodcut = list(sample_prodcut)
sample_prodcut[1] = 15999
sample_prodcut = tuple(sample_prodcut)
print("Updated tuple", sample_prodcut)