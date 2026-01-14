#!/usr/bin/python3
"""
checkbook.py

A simple command-line checkbook simulator. Users can:
- Deposit money
- Withdraw money
- Check their balance
- Exit the program

The Checkbook class tracks the balance and provides methods for transactions.
"""

class Checkbook:
    """
    Represents a simple checkbook with deposit, withdrawal, and balance functionality.
    """
    def __init__(self):
        """
        Initializes a new checkbook with a balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds money to the checkbook balance.

        Args:
            amount (float): The amount to deposit
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Deducts money from the checkbook balance if sufficient funds exist.

        Args:
            amount (float): The amount to withdraw
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main interactive loop for the checkbook application.
    Accepts user input to deposit, withdraw, check balance, or exit.
    """
    cb = Checkbook()  # Create a new checkbook instance

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        if action.lower() == 'exit':
            # Exit the program
            print("Exiting. Goodbye!")
            break
        elif action.lower() == 'deposit':
            # Deposit money
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action.lower() == 'withdraw':
            # Withdraw money
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action.lower() == 'balance':
            # Show current balance
            cb.get_balance()
        else:
            # Invalid command
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    # Run the checkbook program
    main()
