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
        self.validate_number(amount)

    def validate_number(self, number):
        """Validates that a deposit or withdrawal is an integer or float"""
        if not isinstance(number, (int, float)):
            raise Exception('Must be a number')
