def convert_to_npr(dollars, rate=152.58):
    return dollars * rate

npr1 = convert_to_npr(5, 152.58)
npr2 = convert_to_npr(50, 152.58)
npr3 = convert_to_npr(500, 152.58)

print("5$ in nepali rupees is: ", npr1)
print("50$ in nepali rupees is: ", npr2)
print("500$ in nepali rupees is: ", npr3)