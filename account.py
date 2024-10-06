class BankAccount:
    # Class variable for interest rate
    interest_rate = 0.05

    def __init__(self, account_holder):
        # Instance variables
        self.account_holder = account_holder
        self.balance = 0  # Initial balance set to zero

    def deposit(self, amount):
        """Adds the amount to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtracts the amount from the balance if there are sufficient funds."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def apply_interest(self):
        """Adds interest to the current balance based on the interest rate."""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Interest applied. New balance: {self.balance}")

    def display_account_info(self):
        """Displays the account holder’s name and the current balance."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance:.2f}")

# Creating two instances of BankAccount
account1 = BankAccount("Alice")
account2 = BankAccount("Bob")

# Performing deposits and withdrawals for account1
account1.deposit(500)
account1.withdraw(200)

# Performing deposits and withdrawals for account2
account2.deposit(300)
account2.withdraw(100)

# Applying interest
account1.apply_interest()
account2.apply_interest()

# Displaying account information for each account
account1.display_account_info()
account2.display_account_info()
