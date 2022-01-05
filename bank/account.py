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
            'type': 'credit',
            'amount': amount,
            'date': datetime.datetime.now().strftime('%d/%m/%Y')
        })

    def withdraw(self, amount):
        self.__validate_number(amount)
        if self.balance < amount: raise Exception('Insufficient funds')
        self.balance -= amount
        self.__transactions.append({
            'type': 'debit',
            'amount': amount,
            'date': datetime.datetime.now().strftime('%d/%m/%Y')
        })

    def view_statement(self):
        print('date || credit || debit || balance')
        transactions = self.__add_balance()
        for tr in transactions:
            if tr['type'] == 'credit': 
                print("%s || £%.2f || || £%.2f" %(tr['date'], tr['amount'], tr['balance']))
            elif tr['type'] == 'debit': 
                print("%s || || £%.2f || £%.2f" %(tr['date'], tr['amount'], tr['balance']))

    def __add_balance(self):
        balance = 0
        transactions = []
        for tr in self.__transactions:
            if tr['type'] == 'credit': balance += tr['amount']
            if tr['type'] == 'debit': balance -= tr['amount']
            tr['balance'] = balance
            transactions.append(tr)
        return transactions[::-1]

    def __validate_number(self, number):
        if not isinstance(number, (int, float)): 
            raise Exception('Must be a number')
