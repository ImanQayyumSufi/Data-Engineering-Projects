# The main function to take input from the user

from calculator import *

print("Welcome to the car loan affordability calculator.\nWe only have these brands in our data base:")
print("")
for key, value in maintenance_costs.items():
    print(key, end=", ")
print("")

n = int(input("Enter number of cars you want to compare: "))
total_costs = {}

for i in range(n):
    car_brand = input("Enter the name of the car listed in our database: ").capitalize()
    if car_brand not in maintenance_costs.keys():
        print("Car not available")
    monthly_maintenance_cost = get_maintenance_cost(car_brand)
    monthly_gas_cost = get_monthly_gas_cost()
    monthly_installments = get_monthly_interest_rate()

    total_monthly_cost = monthly_maintenance_cost + monthly_gas_cost + monthly_installments
    total_costs[car_brand] = total_monthly_cost
    print(f"You will pay a monthly maintenance cost of: RM{monthly_maintenance_cost:.2f}") # change to 2dp
    print(f"You will pay a monthly gas cost of: RM{monthly_gas_cost:.2f}")
    print(f"You will pay a monthly installment of: RM{monthly_installments:.2f}")
    print("")
    print(f"The total monthly for this car will be: RM{total_monthly_cost:.2f}")

print("The total monthly breakdown of all cars is: ")
for key, value in total_costs.items():
    print(key.capitalize(),":RM",value:.2f)