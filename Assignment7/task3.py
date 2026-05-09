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

class ElectonicProduct(Product):
    def __init__(self, name: str, price: int, category: str, warranty : int):
        super().__init__(name, price, category)

        self.warranty_year = warranty

    def get_info(self):
        print("Details of product")
        print(f"Name     : {self.name}")
        print(f"Price    : {self.get_price()}")
        print(f"Category : {self.category}")
        print(f"Warranty year : {self.warranty_year}")




if __name__ == "__main__":
    p1 = Product('soap', 29, 'beauty')
    p1.get_info()

    p2 = ElectonicProduct("S25 Ultra", 29999, "mobile", 2029)
    p2.get_info()