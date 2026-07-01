meter_reading_before = 500
meter_reading_current = 800

unit_consumed = (meter_reading_current)-(meter_reading_before)
price_per_unit= 12

bill=float(unit_consumed*price_per_unit)
commission_percentange=0.5
bill_with_commission= float(bill+(bill * commission_percentange))
print("The total bill is: ", bill_with_commission)