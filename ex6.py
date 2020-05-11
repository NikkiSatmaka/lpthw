# Assign value to the variable with data type int
types_of_people = 10
# Assign value to the variable with data type string after using string formatting
x = f"There are {types_of_people} types of people."

# Assign value to the variable with data type string
binary = "binary"
# Assign value to the variable with data type string
do_not = "don't"
# Print the string after using string formatting
y = f"Those who know {binary} and those who {do_not}" # string inside a string 1

# Print the variable
print(x)
# Print the variable
print(y)

# Print the string after using string formatting
print(f"I said: {x}") # string inside a string 2
# Print the string after using string formatting
print(f"I also said: '{y}'") # string inside a string 3

# Assign value to the variable with data type bool
hilarious = False
# Assign value to the variable with data type string
joke_evaluation = "Isn't that joke so funny?! {}"

# Print the string after using string formatting
print(joke_evaluation.format(hilarious))

# Assign value to the variable with data type string
w = "This is the left side of..."
# Assign value to the variable with data type string
e = "a string with a right side."

# Print the concatenation of the variables that are strings
print(w + hilarious)
