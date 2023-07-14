#!/usr/bin/python3
"""Bank Account Module.

This module defines the Bankaccount class representing a bank account. It provides methods
to deposit and withdraw funds, as well as retrieve the current account balance.
"""

class Bankaccount:
    """Define the Bankaccount class"""

    def __init__(self, account, balance=0):
        """Initialize a bank account.

        Args:
            account (str): The bank account number.
            balance (float): The initial account balance.
        """
        self.account = account
        self.balance = balance

    def deposit(self, amount):
        """Deposit funds into the account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            float: The updated account balance.
        Raises:
            TypeError: If the amount is not an integer or float.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("The amount must be an integer or float")
        else:
            self.balance = self.balance + amount
            return self.balance

    def withdraw(self, amount):
        """Withdraw funds from the account.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            float: The updated account balance, if successful.

        Raises:
            ValueError: If the balance is insufficient for withdrawal.
        """
        if self.balance > amount:
            self.balance = self.balance - amount
            return self.balance
        else:
            print("Insufficient balance.")

    def get_balance(self):
        """Get the current account balance.

        Returns:
            float: The current account balance.
        """
        return self.balance


# Create an instance of the Bankaccount class
first = Bankaccount('12345', 100000)

print(first.deposit(100000))
print()
print(first.deposit(300000))
print(first.get_balance())

