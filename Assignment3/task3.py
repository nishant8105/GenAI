gst = lambda price : price + (price * 0.18)
discount = lambda price, discount : price - (price * discount / 100)
final_price = lambda price, discount : gst(price) - (gst(price) * discount / 100)

print(gst(100))
print(discount(1000, 10))
print(final_price(1000, 10))