# This file contains all the calculations
from costOfMaintenance import maintenance_costs

def get_monthly_interest_rate():
    principal = float(input("Enter principal amount (RM): "))
    interest_rate = float(input("Enter interest rate (%): "))
    duration = int(input("Enter loan duration (Years): "))
    down_payment = float(input("Enter downpayment amount (RM): "))

    total_interest = interest_rate/100 * (principal-down_payment) * duration
    monthly_installment = (principal-down_payment+total_interest)/(duration*12)

    return print(monthly_installment)

def get_monthly_gas_cost():
    gas_price = 2.05 #RM per litre
    mileage = float(input("Enter average weekly mileage (km) that you drive: "))
    miles_month = mileage*4
    drive_distance = 12.5 #km per litre

    gas_cost = miles_month / drive_distance * gas_price

    return gas_cost

def get_maintenance_cost(car_brand):
    road_tax = float(input("Enter road tax amount (RM): "))
    insurance = float(input("Enter insurance amount (RM): "))
    parking_tolls = float(input("Enter parking/tolls amount per month (RM): "))

    rt = road_tax/12
    ins = insurance/12 #divided by 12 to get cost per month
    total_maintenance = rt + ins + maintenance_costs[car_brand]

    return total_maintenance

    