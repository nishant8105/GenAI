try :
    numerator = int(input("Enter the number: "))
    denominator = int(input("Enter the number: "))
    division = numerator/denominator
    print(f"Division of {numerator} and {denominator} is {division}")
except ZeroDivisionError as zero:
    print('Error : Cannot ', zero)
except ValueError as value :
    print('Error : Please enter valid integer only! \n', value)
finally :
    print("Operation Complete")