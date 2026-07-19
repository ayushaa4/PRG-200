trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

for trip in trips:

    if trip["distance"] <= 2:
        fare = 150

    elif trip["distance"] <= 10:
        fare = 150 + (trip["distance"] - 2) * 35

    else:
        fare = 430 + (trip["distance"] - 10) * 28

    if trip["hour"] >= 22 or trip["hour"] < 5:
        fare = fare + fare * 0.10

    print("Distance:", trip["distance"])
    print("Hour:", trip["hour"])
    print("Fare: NPR", fare)
    print()