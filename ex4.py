# Assign value to the variable with data type integer
cars = 100
# Assign value to the variable with data type float
space_in_a_car = 4.0 # This makes the number a float type. Not necessary
# Assign value to the variable with data type integer
drivers = 30
# Assign value to the variable with data type integer
passengers = 90
# Assign value to the variable after doing arithmetic operations between variables
cars_not_driven = cars - drivers
# Assign value to the variable after doing arithmetic operations between variables
cars_driven = drivers
# Assign value to the variable after doing arithmetic operations between variables
carpool_capacity = cars_driven * space_in_a_car
# Assign value to the variable after doing arithmetic operations between variables
average_passengers_per_car = passengers / cars_driven

# Line 10 will produce an error because there is no variable
# car_pool_capacity
# average_passengers_per_car = car_pool_capacity / passenger


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
