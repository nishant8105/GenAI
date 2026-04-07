file = input("Enter file name : ")
# for test use task1.py file

try :
    file = open(file , "r")
    content = file.readlines()
    for i in range(3):
        print(content[i])
    file.close()
except FileNotFoundError as e :
    print(f"File mot  found {e}")
except PermissionError as p :
    print(f"Permission not granted {p}")
finally :
    print("File operation attempted")