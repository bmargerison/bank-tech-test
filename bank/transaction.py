"""
Creates a transaction instance for storage on a user's account
"""

import datetime

class Transaction:

    def __init__(self, type, amount, balance):
        self.type = type
        self.amount = amount
        self.date = datetime.datetime.now().strftime('%d/%m/%Y')
        self.balance = balance
        self.validate_number(amount)

    def validate_number(self, number):
        """Validates that a deposit or withdrawal is an integer or float"""
        if not isinstance(number, (int, float)):
            raise Exception('Must be a number')
