import os

# Ask user for filename
filename = input("Enter the file name to open: ")

# Check if file exists
if os.path.exists(filename):
    with open(filename, 'r') as f:
        content = f.read()
    print("\n--- File Content ---")
    print(content)
else:
    print("File not found. Please Check the filename.")