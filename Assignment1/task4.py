products = ["Laptop", "Headphones", "Keyboard", "Mouse", "Monitor", "Webcam"]
price_dict= {
    "Laptop" : 84999.34,
    "Headphones" : 1289.56, 
    "Keyboard" : 789, 
    "Mouse" : 299, 
    "Monitor" : 25499, 
    "Webcam" : 1299}

catalog = [
    ('Laptop', 84999.34, 'Computing'),
    ('Headphones', 1289.56, 'Audio'),
    ('Keyboard', 789, 'Accessories'),
    ('Mouse', 299, 'Accessories'),
    ('Monitor', 25499, 'Display'),
    ('Webcam', 1299, 'Peripherals')
]
category_to_products = {}

for name , price, category in catalog :
    if category not in category_to_products :
        category_to_products[category] = []
    category_to_products[category] = ([name, price])

for category, item in category_to_products.items():
    print(f"{category} : {item}")