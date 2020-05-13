# from the package 'sys' import the module argv
from sys import argv

# Unpack the argv
script, user_name, title = argv
# Assign value to the variable with data type string
prompt = '> '

# Print the string after using string formatting
print(f"Hi {user_name} {title}, I'm the {script} script.")
# Print the string
print("I'd like to ask you a few questions.")
# Print the string after using string formatting
print(f"Do you like me {user_name} {title}?")
# Take an input with $rompt and assign it to a variable
likes = input(prompt)

# Print the string after using string formatting
print(f"Where do you live {user_name} {title}?")
# Take an input with prompt and assign it to a variable
lives = input(prompt)

# Print the string after using string formatting
print(f"What kind of computer do you have?")
# Take an input with prompt and assign it to a variable
computer = input(prompt)

# Print the string after using string formatting and double quoted string
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
