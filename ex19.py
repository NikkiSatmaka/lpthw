def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# call the function with arguments using numbers directly
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# call the function with arguments using variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# call the function with arguments using arithmetic operations
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# call the function with arguments using variables and arithmetic operations
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
