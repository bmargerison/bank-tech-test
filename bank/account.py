class Account:

    def __init__(self):
        self.balance = 0.0
        self.__transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.__transactions.append(['credit', amount])

    def withdraw(self, amount):
        self.balance -= amount
        self.__transactions.append(['debit', amount])

    def view_statement(self):
        print('credit || debit || balance')
        running_total = 0
        for transaction in self.__transactions:
            if transaction[0] == 'credit':
                running_total += transaction[1]
                print("£%.2f || || £%.2f" %(transaction[1], running_total))
            elif transaction[0] == 'debit':
                print(running_total)
                running_total -= transaction[1]
                print(" || £%.2f || £%.2f" %(transaction[1], running_total))
