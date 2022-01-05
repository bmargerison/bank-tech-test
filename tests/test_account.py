from bank.account import Account
import re
import pytest

@pytest.fixture
def account():
    account = Account()
    yield account

@pytest.fixture
def account_deposit(account):
    account.deposit(20)
    yield account

@pytest.fixture
def account_withdraw(account_deposit):
    account_deposit.withdraw(5)
    yield account_deposit

def test_account(account):
    assert isinstance(account, Account)

def test_deposit(account_deposit):
    assert account_deposit.balance == 20

def test_withdraw(account_withdraw):
    assert account_withdraw.balance == 15

def test_display_balance(capfd, account_withdraw):
    account_withdraw.view_statement()
    statement, err = capfd.readouterr()
    assert "credit" in statement
    assert "debit" in statement
    assert "balance" in statement
    assert "£15.00" in statement

def test_display_dates(capfd, account_withdraw):
    account_withdraw.view_statement()
    statement, err = capfd.readouterr()
    pattern = '.*?(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}.*?'
    assert "date" in statement
    assert isinstance(re.search(pattern, statement), re.Match)

def test_display_balance_reverse_order(capfd, account_withdraw):
    account_withdraw.view_statement()
    statement, err = capfd.readouterr()
    assert isinstance(re.search('£15.00.*?\n.*?£20.00', statement), re.Match)

def test_balance_cannot_go_below_nil(account):
    with pytest.raises(Exception, match='Insufficient funds'):
        account.withdraw(5)
    
def test_deposit_must_be_int_or_float(account):
    with pytest.raises(Exception, match='Must be a number'):
        account.deposit('money')

def test_withdrawal_must_be_int_or_float(account):
    with pytest.raises(Exception, match='Must be a number'):
        account.withdraw('money')