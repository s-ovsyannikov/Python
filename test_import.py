import math

initial_deposit = 100000
rate = 15
years = 5
final_ammount = initial_deposit * math.exp((rate / 100) * years)
print(final_ammount)
