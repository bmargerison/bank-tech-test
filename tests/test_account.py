from bank.account import Account
import re
import pytest

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
    assert "credit" in statement
    assert "debit" in statement
    assert "balance" in statement
    assert "£15.00" in statement

def test_display_balance_reverse_order(capfd):
    account = Account()
    account.deposit(20)
    account.withdraw(5)
    account.view_statement()
    statement, err = capfd.readouterr()
    assert isinstance(re.search('£15.00.*?\n.*?£20.00', statement), re.Match)

def test_balance_cannot_go_below_nil():
    account = Account()
    with pytest.raises(Exception, match='Insufficient funds'):
        account.withdraw(5)
    
def test_deposit_must_be_int_or_float():
    account = Account()
    with pytest.raises(Exception, match='Must be a number'):
        account.deposit('money')