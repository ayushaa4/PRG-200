passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

for password in passwords:
    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:
        if ch.isupper():
            upper = True
        if ch.islower():
            lower = True
        if ch.isdigit():
            digit = True
        if ch in "!@#$%^&*":
            special = True

    if len(password) >= 8 and upper and lower and digit and special:
        print(password, "- Strong Password")
    else:
        print(password, "- Weak Password")

        if len(password) < 8:
            print("Missing: At least 8 characters")

        if not upper:
            print("Missing: Uppercase letter")

        if not lower:
            print("Missing: Lowercase letter")

        if not digit:
            print("Missing: Digit")

        if not special:
            print("Missing: Special character")

    print()