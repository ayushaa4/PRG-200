cost_price=100
selling_price=180

profit= selling_price-cost_price
plates_per_day= int(input("Enter how much plates sold per day: "))
profit_per_day= plates_per_day*profit

profit_per_month= profit_per_day *30
print("Total profit is: ", profit_per_month)