class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        self.get_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            confirm = input(f"Are you sure you want to withdraw ${amount:.2f}? (yes/no): ").lower()
            if confirm == 'yes':
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}")
                self.get_balance()
            else:
                print("Withdrawal cancelled.")

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    print("Welcome to the Checkbook Application!")
    print("You can deposit, withdraw, check your balance, or exit the program.")
    cb = Checkbook()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Thank you for using the Checkbook Application. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
