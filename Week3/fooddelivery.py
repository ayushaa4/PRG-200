orders = [
    ("Order101", 30),
    ("Order102", 15),
    ("Order103", 25),
    ("Order104", 10)
]

orders.sort(key=lambda x: x[1])

print("Orders sorted by delivery time:")

for order in orders:
    print(order)