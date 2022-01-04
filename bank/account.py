class Account:

    def __init__(self):
        self.balance = 0.0
        self.__transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.__transactions.append({
            'type': 'credit',
            'amount': amount
        })

    def withdraw(self, amount):
        self.balance -= amount
        self.__transactions.append({
            'type': 'debit',
            'amount': amount
        })

    def view_statement(self):
        print('credit || debit || balance')
        transactions = self.__add_balance()
        for tr in transactions:
            if tr['type'] == 'credit': 
                print("£%.2f || || £%.2f" %(tr['amount'], tr['balance']))
            elif tr['type'] == 'debit': 
                print(" || £%.2f || £%.2f" %(tr['amount'], tr['balance']))

    def __add_balance(self):
        balance = 0
        transactions = []
        for tr in self.__transactions:
            if tr['type'] == 'credit': balance += tr['amount']
            if tr['type'] == 'debit': balance -= tr['amount']
            tr['balance'] = balance
            transactions.append(tr)
        return transactions[::-1]
