money = float(input("Enter the money recieved: "))
Qatar_in_nrp= 41.41
currency_in_nrp= float(money*(41.41))

Service_percentage= 0.5
after_commission= float(currency_in_nrp-(Service_percentage*currency_in_nrp))
print("Actual money recieved is: ",after_commission)