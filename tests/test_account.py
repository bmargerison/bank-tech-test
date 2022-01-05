"""
Testing the Account() class
"""

import re
import pytest
from bank.account import Account

@pytest.fixture(name="account")
def fixture_account():
    """Creates an instance of Account() class"""
    account = Account()
    yield account

@pytest.fixture(name="account_deposit")
def fixture_account_deposit():
    """Creates an instance of Account class and deposits funds"""
    account = Account()
    account.deposit(20)
    yield account

@pytest.fixture(name="account_withdraw")
def fixture_account_withdraw():
    """Creates an instance of Account class and deposits and withdraws funds"""
    account = Account()
    account.deposit(20)
    account.withdraw(5)
    yield account

def test_account(account):
    """Can create a new instance of Account"""
    assert isinstance(account, Account)

def test_deposit(account_deposit):
    """Can deposit funds to an account"""
    assert account_deposit.balance == 20

def test_withdraw(account_withdraw):
    """Can withdraw funds from an account"""
    assert account_withdraw.balance == 15

@pytest.mark.parametrize("text", ["credit",
    "debit",
    "balance",
    "15.00",
    "date"])

def test_display_balance(capfd, account_withdraw, text):
    """Prints out a statement to the console"""
    account_withdraw.view_statement()
    statement = capfd.readouterr().out
    assert text in statement

def test_date_format(capfd, account_withdraw):
    """The date is printed in the format DD/MM/YYYY"""
    account_withdraw.view_statement()
    statement = capfd.readouterr().out
    regex = r'.*?(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}.*?'
    assert isinstance(re.search(regex, statement), re.Match)

def test_display_balance_newest_to_oldest(capfd, account_withdraw):
    """Transactions are displayed from newest to oldest"""
    account_withdraw.view_statement()
    statement = statement = capfd.readouterr().out
    assert isinstance(re.search('15.00.*?\n.*?20.00', statement), re.Match)

def test_balance_cannot_go_below_nil(account):
    """Cannot withdraw below nil balance"""
    with pytest.raises(Exception, match='Insufficient funds'):
        account.withdraw(5)

def test_deposit_must_be_int_or_float(account):
    """A deposit must be an integer or float"""
    with pytest.raises(Exception, match='Must be a number'):
        account.deposit('money')

def test_withdrawal_must_be_int_or_float(account):
    """A withdrawal must be an integer or float"""
    with pytest.raises(Exception, match='Must be a number'):
        account.withdraw('money')
