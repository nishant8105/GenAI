from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):

    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ₹{amount}")


class UPIPayment(Payment):

    def process_payment(self, amount):
        print(f"Processing UPI payment of ₹{amount}")


credit_payment = CreditCardPayment()
upi_payment = UPIPayment()

credit_payment.process_payment(5000)
upi_payment.process_payment(1500)