"""
Allows the user to create an account, deposit and withdraw funds, and view their
transaction history.
"""

from bank.transaction import Transaction

class Account:
    """Deposit funds, withdraw funds, view transactions history"""

    def __init__(self):
        """Account instance stores current balance and transaction history"""
        self.balance = 0.0
        self.__transactions = []

    def deposit(self, amount):
        """User can despoit funds to their account"""
        self.balance += amount
        self.__transactions.append(Transaction('cr', amount, self.balance))

    def withdraw(self, amount):
        """User can withdraw funds from their account"""
        if self.balance < amount:
            raise Exception('Insufficient funds')
        self.balance -= amount
        self.__transactions.append(Transaction('dr', amount, self.balance))

    def view_statement(self):
        """User can view their statement showing transaction history"""
        print('date || credit || debit || balance')
        for transaction in self.__transactions[::-1]:
            amount = format(transaction.amount, '.2f')
            balance = format(transaction.balance, '.2f')
            if transaction.type == 'cr':
                print(f"{transaction.date} || {amount} || || {balance}")
            elif transaction.type == 'dr':
                print(f"{transaction.date} || || {amount} || {balance}")
