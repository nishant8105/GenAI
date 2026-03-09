prodcuts = ["Samsung S22", "HP Victus", "Lenovo LOQ", "Iphone 17", "Samsung Book 5", "Oppo A7"]
sample_prodcut = ("Samsung S22", 12999, "Phone")

# print 2nd and last product from list
print("2nd product",prodcuts[1], "last product", prodcuts[-1])

# append 2 prodcuts
prodcuts.append("Realme 7")
prodcuts.append("Samsung S26 Ultra")

# print updated list
print("Updated list", prodcuts)

# optional
sample_prodcut = list(sample_prodcut)
sample_prodcut[1] = 15999
sample_prodcut = tuple(sample_prodcut)