class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total: {self.total_price()}")
        print("-" * 30)

    def __add__(self, other):
        return self.total_price() + other.total_price()


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added successfully.")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} removed successfully.")
                return
        print(f"{name} not found.")

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.total_price()
        return total

    def show_all_products(self):
        print("\nAll Products:")
        print("=" * 30)
        for product in self.products:
            product.display_info()


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        product = Product(name, price, quantity)
        self.inventory.add_product(product)

    def show_summary(self):
        print("\nStore Summary")
        print("=" * 30)
        print(f"Store Name: {self.store_name}")
        print(f"Total Items: {len(self.inventory.products)}")
        print(f"Total Inventory Value: {self.inventory.get_total_value()}")


store = Store("Tech Mart")

p1 = Product("Laptop", 800, 2)
p2 = Product("Mouse", 20, 5)
p3 = Product("Keyboard", 50, 3)

store.inventory.add_product(p1)
store.inventory.add_product(p2)
store.inventory.add_product(p3)

store.inventory.show_all_products()

store.show_summary()

combined_price = p1 + p2
print("\nCombined Total Price of Laptop and Mouse:", combined_price)