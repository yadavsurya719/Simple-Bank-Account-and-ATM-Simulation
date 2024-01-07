class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive value."
        else:
            return "Insufficient funds. Withdrawal amount exceeds your balance."


def main():
    # Create a sample bank account
    account_number = "123456789"
    account_holder = "John Doe"
    initial_balance = 10000
    account = BankAccount(account_number, account_holder, initial_balance)

    while True:
        print("\nATM Simulation:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(account.check_balance())
        elif choice == "2":
            amount = float(input("Enter the deposit amount: "))
            print(account.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            print(account.withdraw(amount))
        elif choice == "4":
            print("Exiting ATM simulation. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
