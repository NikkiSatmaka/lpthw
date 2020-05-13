# from the module 'sys' import the dynamict object argv
from sys import argv
# read the WYSS section for how to run this
# Unpack the argv
script, first, second, third = argv
fourth = input("Okay, what about the fourth variable? ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)
