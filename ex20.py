from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')


# Open the variable file and assign it to a variable
current_file = open(input_file)

print("First let's print the whole file:\n")

# Call the function
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Call the function
rewind(current_file)

print("Let's print three lines:")

# Assign value 1 to the variable current_line
current_line = 1
# current_line = 1
# Call the function
print_a_line(current_line, current_file)

# Add the variable current_line by 1 and assign it to variable current_line
current_line = current_line + 1
# current_line = 2
# Call the function
print_a_line(current_line, current_file)

# Add the variable current_line by 1 and assign it to variable current_line
current_line = current_line + 1
# current_line = 3
# Call the function
print_a_line(current_line, current_file)
