from task3 import Product

class Laptop(Product):
    def __init__(self, name: str, price: int, category: str, ram: int):
        super().__init__(name, price, category)
        self.ram = ram

    def get_info(self):
        print("Details of product")
        print(f"Name     : {self.name}")
        print(f"Price    : {self.get_price()}")
        print(f"Category : {self.category}")
        print(f"Ram      : {self.ram} GB")

class Mobile(Product):
    def __init__(self, name: str, price: int, category: str, camera : int) -> None:
        super().__init__(name, price, category)
        self.camera = camera

    def get_info(self):
        print("Details of product")
        print(f"Name     : {self.name}")
        print(f"Price    : {self.get_price()}")
        print(f"Category : {self.category}")
        print(f"Camera   : {self.camera} Mega Pixel")

l1 = Laptop("HP Victus", 77000, "Laptop", 16)
m1 = Mobile("Sumsung A22 5G", 21599, "Mobile", 50)

# products act as single class
products = [l1, m1]

for item in products:
    item.get_info()
    print("-------------------")