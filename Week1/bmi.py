weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in cm: "))

height = height / 100

bmi = weight / (height ** 2)

print("BMI is:", round(bmi,1))