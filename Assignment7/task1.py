class Product :
    def __init__(self, name:str, price: int, category: str) -> None:
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        print("Details of product")
        print(f"Name     : {self.name}")
        print(f"Price    : {self.price}")
        print(f"Category : {self.category}")
    
    def apply_discount(self, discount : int) :
        self.discount = discount
        discounted_price = self.price - (self.price*(self.discount/100))
        return discounted_price
    

p1 = Product('soap', 29, 'beauty')
p1.get_info()
print(f"Discounted price : {p1.apply_discount(15)}")


p2 = Product('Sprite', 25, 'beverage')
p2.get_info()
print(f"Discounted price : {p2.apply_discount(15)}")