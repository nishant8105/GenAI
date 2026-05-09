class Product :
    def __init__(self, name:str, price: int, category: str) -> None:
        self.name = name
        self.__price = price
        self.category = category
    
    def get_info(self):
        print("Details of product")
        print(f"Name     : {self.name}")
        print(f"Price    : {self.__price}")
        print(f"Category : {self.category}")
    
    def apply_discount(self, discount : int) :
        self.discount = discount
        discounted_price = self.__price - (self.__price*(self.discount/100))
        return discounted_price
    
    def get_price(self):
        return self.__price
    
    def set_price(self, new_price : int):
        if new_price > 0 :
            self.__price = new_price
            print(f"price is updated to {self.__price}")
        else :
            print("New price should be > 0")

    def __str__(self):
        return f"Product({self.name, self.__price, self.category})"
    
    def __add__(self, other):
        return self.__price + other.__price
    
p1 = Product('Laptop', 77000, "Electronics")
p2 = Product("Phone", 21000, 'Electronics')

print(p1)
print(p2)

total_price = p1 + p2
print("Combined Price: ", total_price)