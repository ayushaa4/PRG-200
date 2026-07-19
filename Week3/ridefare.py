def estimate_fare(distance_km, vehicle_type, surge=1.0):

    rates = {
        "economy": 15,
        "standard": 20,
        "premium": 30
    }

    rate = rates.get(vehicle_type.lower(), 20)
    
    return distance_km * rate * surge

print("Economy Fare:", estimate_fare(10, "economy"))
print("Standard Fare:", estimate_fare(10, "standard"))
print("Premium Fare:", estimate_fare(10, "premium"))
print("Premium Fare with Surge:", estimate_fare(10, "premium", 1.5))