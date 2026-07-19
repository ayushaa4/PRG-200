purchase = float(input("Enter purchase amount: "))
member = input("Are you a loyalty member? (yes/no): ")

if purchase < 1000:
    discount = 0

elif purchase < 5000:
    discount = 5

elif purchase < 15000:
    discount = 10

else:
    discount = 20

final = purchase - (purchase * discount / 100)

if member == "yes":
    final = final - (final * 5 / 100)

print("Final payable amount: NPR", final)