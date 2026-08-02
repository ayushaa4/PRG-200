class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Insufficient funds for {self.name}")

    def get_balance(self):
        print(f"{self.name} ({self.account_number}) - Balance: NPR {self.balance}")


accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]

bank_accounts = []

for name, acc_no, balance in accounts:
    bank_accounts.append(BankAccount(name, acc_no, balance))

bank_accounts[1].deposit(3000)
bank_accounts[2].withdraw(15000)
bank_accounts[0].withdraw(2000)

print("\nFinal Balances:")
for account in bank_accounts:
    account.get_balance()