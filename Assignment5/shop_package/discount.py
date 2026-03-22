def apply_discount(price, percent):
    price -= (price * (percent / 100))

    return price

def flat_discount(price):
    return price - 50