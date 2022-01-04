from bank.account import Account

def test_account():
    account = Account()
    assert isinstance(account, Account)

def test_deposit():
    account = Account()
    account.deposit(20)
    assert account.balance == 20
