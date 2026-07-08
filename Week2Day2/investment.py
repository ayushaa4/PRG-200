companies= []

for i in range(9):
    company_name = input("Enter company name: ")
    buying_price = int(input("Enter buying price: "))
    selling_price = int(input("Enter selling price: "))

    company={
        "name": company_name,
        "buying_price": buying_price,
        "selling_price": selling_price 
    }

    companies.append(company)

print("\n Investment Results \n")

for c in companies:
    name = c["name"]
    buying = c["buying_price"]
    selling = c["selling_price"]
    
    difference = selling - buying
    
    if difference > 0:
        print(f"{name}: Profit of {difference}")
    elif difference < 0:
        print(f"{name}: Loss of {(difference)}")
    else:
        print(f"{name}: No Profit NO Loss")
