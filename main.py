# The main function to take input from the user

from calculator import *

print("Welcome to the car loan affordability calculator.\nWe only have these brands in our data base:")

for key, value in maintenance_costs.items():
    print(key, end=", ")
print("")