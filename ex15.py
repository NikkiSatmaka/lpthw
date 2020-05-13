# from the package 'sys' import the module argv
from sys import argv

# Unpack the argv
script, filename = argv

# Open the variable file and assign it to a variable
txt = open(filename)

# Print the string after using string formatting
print(f"Here's your file {filename}:")
# Read the file and run the function read, then print the output
print(txt.read())
# Run the close function on the variable
txt.close()

# Print the string
print("Type the filename again:")
# Take an input and assign it to a variable
file_again = input("> ")

# Open the variable file and assign it to a variable
txt_again = open(file_again)

# Read the file and run the function read, then print the output
print(txt_again.read())
# Run the close function on the variable
txt_again.close()
