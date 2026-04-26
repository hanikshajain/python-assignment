class BankAccount:
    
    # Constructor
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    # Withdraw method
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{self.balance}")

    # Check balance method
    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# Create object
account1 = BankAccount("1234567890", 1000)

# Perform operations
account1.deposit(500)
account1.withdraw(300)
account1.check_balance()