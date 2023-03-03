from src.piracy import (Captain, Ship)
import pytest

# test Captain class arguments to onlt accept the appropriate data types
def test_it_raises_DataType_error_when_invalid_datatype_is_passed_on():
    with pytest.raises(TypeError, match='Invalid input'):
        test_captain = Captain('alex', 'al', '10', 'hahahahahah')
    with pytest.raises(TypeError, match='Invalid input'):
        test_captain = Captain('alex', 12, 10, 'hahahahahah')
    with pytest.raises(TypeError, match='Invalid input'):
        test_captain = Captain('alex', '12', 10, 15)
    with pytest.raises(TypeError, match='Invalid input'):
        test_captain = Captain(1, '12,', 10, 'hahahahahah')

# test Captain class arguments to onlt accepts the appropriate valuse
    
# test Captin holds the appropriate constructor attributes/properties 

def test_Captain_holds_the_appropriate_constructor_properties():
    test_captain = Captain('alex', 'al', 10 , 'hahahahahah')
    assert test_captain.name == 'alex'
    assert test_captain.nickname == 'al'
    assert test_captain.crew_size == 10
    assert test_captain.catchphrase == 'hahahahahah'

# test ship class holds the apropriate properties 

def test_ship_class_holds_the_appropriate_attributes():
    test_captain = Captain('Mostafa', 'Musty', 6, 'ohhh yeah!')
    test_ship = Ship(20, test_captain)
    assert test_ship.draft == 20
    assert test_ship.crew == 6

def test_ship_worth_it_method():
    test_captain = Captain('Mostafa', 'Musty', 6, 'ohhh yeah!')
    test_ship = Ship(20, test_captain)
    assert test_ship.worth_it() is False
    test_ship = Ship(30, test_captain)
    assert test_ship.worth_it() is True

