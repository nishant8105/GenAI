def calculate_total(prices :list ):
    '''price is always provide list or tuple
    '''
    sum = 0
    for i in prices:
        sum += i

    return sum

def apply_tax(amount):
    tax = amount + (amount * 0.05)
    return tax