class Product :
    def __init__(self,name:str, price:int, category:str):
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


p1 = Product('soap', 29, 'beauty')
print(f"price of your product is {p1.get_price()}")
p1.set_price(35)

p1.__price = 20
print(p1.get_price(),"price not updated therefore price is private(Encapsulated)")

p2 = Product('Sprite', 25, 'beverage')
print(f"price of your product is {p2.get_price()}")
p2.set_price(20)
