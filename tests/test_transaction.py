"""
Testing the Transaction class
"""

import pytest
from bank.transaction import Transaction

def test_deposit_must_be_int_or_float():
    """A deposit must be an integer or float"""
    with pytest.raises(Exception, match='Must be a number'):
        Transaction('cr', 'money', 0.0)

def test_withdrawal_must_be_int_or_float():
    """A withdrawal must be an integer or float"""
    with pytest.raises(Exception, match='Must be a number'):
        Transaction('dr', 'money', 0.0)
