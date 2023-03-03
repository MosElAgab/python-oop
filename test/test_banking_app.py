from src.banking_app import (user)
import pytest

def test_user_holds_current_balance_property():
    new_user = user()
    assert new_user.current_balance == 0
    assert isinstance(new_user.current_balance, float)

def test_user_holds_appropriate_pot_property():
    new_user = user()
    assert new_user.pots == {}

def test_the_functionality_of_user_deposit_money_method():
    new_user = user()
    new_user.deposit_money(3.67)
    assert new_user.current_balance == 3.67

def test_the_functionality_of_user_create_new_pot_method():
    new_user = user()
    new_user.create_new_pot('Holiday')
    print('pots', new_user.pots)
    assert new_user.pots['Holiday']['pot_balance'] == 0
    new_user.create_new_pot('Bussines')
    print('pots', new_user.pots)
    assert new_user.pots['Bussines']['pot_balance'] == 0

def test_the_functionality_of_user_add_to_pot_method():
    new_user = user()
    new_user.create_new_pot('Holiday')
    new_user.create_new_pot('Bussines')
    new_user.add_to_pot('Holiday', 10)
    print('pots', new_user.pots)
    assert new_user.pots['Holiday']['pot_balance'] == 10
    assert isinstance(new_user.pots['Holiday']['pot_balance'], float)
    new_user.add_to_pot('Holiday', 8.4)
    new_user.add_to_pot('Holiday', 11.64)
    new_user.add_to_pot('Bussines', 14.78)
    assert new_user.pots['Holiday']['pot_balance'] == 30.04
    assert new_user.pots['Bussines']['pot_balance'] == 14.78
    with pytest.raises(Exception, match='there is no money pot with this name'):
        new_user.add_to_pot('night life', 11.64)


def test_the_functionality_of_user_transfer_to_pot_method():
    new_user = user()
    new_user.create_new_pot('Holiday')
    new_user.create_new_pot('Bussines')
    new_user.deposit_money(1463.67)
    new_user.transfer_to_pot('Holiday', 400.22)
    assert new_user.pots['Holiday']['pot_balance'] == 400.22
    assert new_user.current_balance == 1063.45