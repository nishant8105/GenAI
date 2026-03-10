products = ["Laptop", "Headphones", "Keyboard", "Mouse", "Monitor", "Webcam"]
categories = ["Electronics", "Audio", "Accessories", "Accessories", "Display", "Accessories"]
categories_set = set(categories)
print("Categories set", categories_set)

categories_set.add("Display")
categories_set.add("Gaming")

print("Updated Categories set", categories_set)
print("\nIs Audio in categories_set ", "Audio" in categories_set)
print("\nTotal number of unique Categories", len(categories_set))