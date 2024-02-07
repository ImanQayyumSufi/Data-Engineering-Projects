# This file contains all the calculations

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

def get_maintenance_cost():
    road tax:
    insurance:
    parking and tolls:

    