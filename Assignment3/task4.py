prices = [100, 250, 400, 1200, 50]
prices_with_gst = list(map(lambda x : x + (x * 0.18), prices))
print(f"original prices: {prices}")
print(f"prices with gst: {prices_with_gst}")