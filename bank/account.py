import re
import datetime

class Account:

    def __init__(self):
        self.balance = 0.0
        self.__transactions = []
    
    def deposit(self, amount):
        self.__validate_number(amount)
        self.balance += amount
        self.__transactions.append({
            'type': 'cr',
            'amount': amount,
            'date': datetime.datetime.now().strftime('%d/%m/%Y'),
            'balance': self.balance
        })

    def withdraw(self, amount):
        self.__validate_number(amount)
        if self.balance < amount: raise Exception('Insufficient funds')
        self.balance -= amount
        self.__transactions.append({
            'type': 'dr',
            'amount': amount,
            'date': datetime.datetime.now().strftime('%d/%m/%Y'),
            'balance': self.balance
        })

    def view_statement(self):
        print('date || credit || debit || balance')
        transactions = self.__transactions[::-1]
        for tr in transactions:
            print_tr = (tr['date'], tr['amount'], tr['balance'])
            if tr['type'] == 'cr': print("%s || £%.2f || || £%.2f" %print_tr)
            elif tr['type'] == 'dr': print("%s || || £%.2f || £%.2f" %print_tr)

    def __validate_number(self, number):
        if not isinstance(number, (int, float)): 
            raise Exception('Must be a number')
