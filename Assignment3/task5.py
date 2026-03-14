prices = [100, 250, 400, 1200, 50, 2000, 850]
greater_than_500 = list(filter(lambda x : x > 500, prices))
less_than_500 = list(filter(lambda x : x < 500, prices))

print(f"prices greater than 500: {greater_than_500}")
print(f"prices less than 500: {less_than_500}")