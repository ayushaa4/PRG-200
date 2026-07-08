fees = []

n = int(input("Enter number of vehicles: "))

for i in range(n):

    vehicle_no = input("Enter vehicle number: ")
    vehicle = input("Enter vehicle type (car/motorcycle): ").lower()
    hours = int(input("Enter parking hours: "))

    if hours <= 2:
        fee = 50
    elif hours <= 5:
        fee = 50 + (hours - 2) * 30
    else:
        fee = 50 + (hours - 2) * 90

    if vehicle == "motorcycle":
        fee = fee * 0.8

    if fee > 500:
        fee += 50

    fees.append(fee)
    print("\nDetails")
    print("Vehicle Number:", vehicle_no)
    print("Vehicle Type:", vehicle)
    print("Parking Fee: Rs.", fee)

print("\nTotal Revenue = Rs.", sum(fees))