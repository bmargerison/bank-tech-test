"""
Creates a transaction instance for storage on a user's account
"""

import datetime

class Transaction:
    """Create new transaction and validates"""

    def __init__(self, tr_type, amount, balance):
        """Transaction type, amount, date and balance"""
        self.tr_type = tr_type
        self.amount = amount
        self.date = datetime.datetime.now().strftime('%d/%m/%Y')
        self.balance = balance
        self.validate_number()
        self.validate_balance()

    def validate_number(self):
        """Validates that a deposit or withdrawal is an integer or float"""
        if not isinstance(self.amount, (int, float)):
            raise Exception('Must be a number')

    def validate_balance(self):
        """Validates that the user has sufficient funds"""
        if self.balance < self.amount:
            raise Exception('Insufficient funds')
