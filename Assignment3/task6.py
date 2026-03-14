def processs_prices(prices):
    discounted_prices = list(map(lambda prices : prices - (prices * 0.10), prices))
    filtered_prices = list(filter(lambda prices : prices > 300, prices))

    return discounted_prices, filtered_prices
discounted_prices, filtered_prices = processs_prices([100, 500, 900, 50, 750])  
print(f"Discounted prices: {discounted_prices}")
print(f"Filtered prices: {filtered_prices}")