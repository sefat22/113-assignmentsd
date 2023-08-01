from account import Account

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance):
        super().__init__(account_number, account_holder, balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance or invalid withdrawal amount.")
