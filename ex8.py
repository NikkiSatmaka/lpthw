formatter = "{} {} {} {}"

# Take the formatter string and call its format function, then pass
# the four arguments
print(formatter.format(1, 2, 3, 4))  # no of args has to match the range
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
