"""Instantiating A Class"""


"""
This is where we instantiate the class we defnied in classes.py
In other words, we're creating objects that belong to that class.
"""

# import the class
# from <file_name>, <module_name> import <class_name>
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) # Constructor

# Make sals_pizza = size M, 5 toppings, not GF

sals_pizza: Pizza = Pizza("medium", 5, False)

"""my_pizza: Pizza = Pizza()  # constructor
my_pizza.size = "large"
my_pizza.size = 10
my_pizza.gluten_free = False"""

print("Size: ")
print(my_pizza.size)

print("my_pizza")
print(my_pizza)

print("Pizza class: ")
print(Pizza)


