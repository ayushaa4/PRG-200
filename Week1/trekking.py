tims_fee = int(input("Enter TIMS fee: "))
acap_fee = int(input("Enter ACAP fee: "))
trekkers = int(input("Enter number of trekkers: "))

total_cost = (tims_fee + acap_fee) * trekkers
service_charge = total_cost * 0.05

final_cost = total_cost + service_charge
average_cost = final_cost / trekkers

print("Final Cost:", final_cost)
print("Average Cost Per Person:", average_cost)