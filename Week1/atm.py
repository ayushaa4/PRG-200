correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter a PIN: ")
    if pin == correct_pin:
        print("PIN correct")
        attempts=3
    else:
        attempts += 1
        if attempts < 3:
            print("PIN incorrect, try again")
        else:
            print("Card blocked")