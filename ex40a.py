# dictionary
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# this goes in mystuff.py
# module
def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine = "Living a reflection of a dream"

# class
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
