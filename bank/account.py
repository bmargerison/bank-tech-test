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
        running_total = 0
        for transaction in self.__transactions:
            if transaction['type'] == 'credit':
                running_total += transaction['amount']
                print("£%.2f || || £%.2f" %(transaction['amount'], running_total))
            elif transaction['type'] == 'debit':
                running_total -= transaction['amount']
                print(" || £%.2f || £%.2f" %(transaction['amount'], running_total))
