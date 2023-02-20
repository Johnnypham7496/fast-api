import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) ==expected

def test_subtract():
    assert subtract(9, 4) ==5

def test_multiply():
    assert multiply(4, 3) ==12

def test_divide():
    assert divide(20, 5) ==4


def test_bank_set_initial_ammount():
    banck_account = BankAccount(50)
    assert banck_account.balance == 50

def test_bank_default_ammount():
    bank_account = BankAccount()
    assert bank_account.balance == 0

def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdraw(20) 
    assert bank_account.balance == 30

def test_deposit():
    bank_account = BankAccount(50)
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_interest():
    bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55