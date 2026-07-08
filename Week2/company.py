rate=5
count=1

print("Comapny Billing System")

while count <=10:
    name= input("Enter the deaprtment's name: ")
    unit= int(input("Enter units consumed: "))

    bill=unit*rate

    print("Department name: ", name)
    print("Bill: ",bill)
    print()

    count+=1