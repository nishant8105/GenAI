def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 to 120")
    return age
try:
    age = int(input("Enter your age: "))
    
    valid_age = check_age(age)
    
    print(f"Valid age entered: {valid_age}")

except ValueError as e:
    print("Error:", e)