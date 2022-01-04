from bank.account import Account

def test_account():
    account = Account()
    assert isinstance(account, Account)

