def recharge_cost(gb, validity_days=30):
    
    if gb == 1:
        return 150
    elif gb == 2:
        return 300
    elif gb == 5:
        return 700
    elif gb == 10:
        return 1050
    elif gb == 20:
        return 1400
    else:
        return ("Invalid GB pack")

print(recharge_cost(1, 30))