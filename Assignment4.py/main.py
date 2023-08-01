from bank import Bank
from savings_account import SavingsAccount
from checking_account import CheckingAccount

def main():
    bank = Bank("My Bank")

    # Create savings and checking accounts
    savings_acc = SavingsAccount("SAV001", "John Doe", 1000, 5)
    checking_acc = CheckingAccount("CHK001", "Jane Smith", 2000)

    # Add accounts to the bank
    bank.add_account(savings_acc)
    bank.add_account(checking_acc)

    # Perform operations on accounts
    savings_acc.deposit(500)
    checking_acc.withdraw(100)
    savings_acc.add_interest()

    # Display account information
    print("Account Information:")
    for account in bank.get_all_accounts():
        account.display_info()
        print("")

if __name__ == "__main__":
    main()
