#!/usr/bin/python3
class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance checks.

    Attributes:
        balance (float): The current balance in the checkbook.
    """

    def __init__(self):
        """
        Initializes a Checkbook instance with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook.

        Args:
            amount (float): The amount of money to deposit.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook.

        Args:
            amount (float): The amount of money to withdraw.

        Raises:
            ValueError: If the withdrawal amount is negative or exceeds the balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Prints the current balance in the checkbook.
        """
        print(f"Current Balance: ${self.balance:.2f}")


def main():
    """
    Main function to interact with the Checkbook class.

    Repeatedly prompts the user for actions until they choose to exit.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Exiting the checkbook application.")
            break
        elif action == 'deposit':
            amount = float(input("Enter the amount to deposit: $").strip())
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $").strip())
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
