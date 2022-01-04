from bank.account import Account

def test_account():
    account = Account()
    assert isinstance(account, Account)

def test_deposit():
    account = Account()
    account.deposit(20)
    assert account.balance == 20

def test_withdraw():
    account = Account()
    account.deposit(20)
    account.withdraw(5)
    assert account.balance == 15

def test_display_balance(capfd):
    account = Account()
    account.deposit(20)
    account.withdraw(5)
    account.view_statement()
    statement, err = capfd.readouterr()
    print(statement)
    assert "credit" in statement
    assert "debit" in statement
    assert "balance" in statement
    assert "£15.00" in statement


