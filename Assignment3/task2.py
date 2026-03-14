def factorial(n):
    try :
        if n < 0 :
            raise ValueError("n must be a non-negative integer")
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    except ValueError as e:
        print(e)
        return None

print(factorial(5))
print(factorial(0))
print(factorial(-3))