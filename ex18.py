# this line is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no argument
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# Function checklist
# 1. Start function definition with def
# 2. Funcation name should only have characters and _ characters
# 3. Put open parenthesis right after function name
# 4. Put arguments after parenthesis separated by commas
# 5. Make each argument unique
# 6. Put close parenthesis and colon after arguments
# 7. Indent all lines of code in function four spaces
# 8. End the function by going back writing with no indent (dedenting)

# Calling function checklist
# 1. Call/use/run function by typing its name
# 2. Put the ( character after the name to run it
# 3. Put the values into the parenthesis separated by commas
# 4. End the function call with a ) character
