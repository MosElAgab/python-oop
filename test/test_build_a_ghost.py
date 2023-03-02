from src.build_a_ghost import (Ghost)
from src.build_a_ghost import (Blinky)
from src.build_a_ghost import (Pinky)
from src.build_a_ghost import (Inky)
from src.build_a_ghost import (Clyde)

def test_ghost_is_constructed_with_the_appropriate_properties():
    test_ghost = Ghost('Ducky', 3, 'yellow')
    assert test_ghost.name == 'Ducky'
    assert test_ghost.speed == 3
    assert test_ghost.colour == 'yellow'

def test_ghost_is_constructed_with_default_false_is_scared_class_attribute():
    test_ghost = Ghost('Ducky', 3, 'yellow')
    assert test_ghost.is_scared is False
    
def test_ghost_can_be_eaten():
    test_ghost = Ghost('Ducky', 6, 'green')
    assert test_ghost.can_be_eaten() is False
    # test_ghost.is_scared = True
    # assert test_ghost.can_be_eaten() is True

def test_ghost_is_frighten_method_changes_colour_and_is_scared_properties():
    ducky = Ghost('ducky', 10, 'green')
    ducky.frighten()
    assert ducky.colour == 'blue'
    assert ducky.is_scared is True

def test_ghost_speed_up_method_increases_speed_by_10_percent():
    ducky = Ghost('ducky', 10, 'green')
    ducky.speed_up()
    assert ducky.speed == 11
    ducky.speed_up()
    ducky.speed_up()
    assert ducky.speed == 13.31

def test_Blinky_Ghost_inheritance_to_all_parrent_class_methods_and_properties():
    test_ghost = Blinky('xx', 2, 'green')
    assert not test_ghost.is_scared
    assert test_ghost.name == 'Blinky'
    assert test_ghost.speed == 3
    assert test_ghost.colour == 'red'
    test_ghost.speed_up()
    assert test_ghost.speed == 3.3
    assert str(test_ghost)== 'This is red Blinky, watch out'
    test_ghost.frighten()
    assert test_ghost.colour == 'blue'
    assert test_ghost.is_scared
    assert test_ghost.can_be_eaten()

def test_Pinky_Ghost_inheritance_to_all_parrent_class_methods_and_properties():
    test_ghost = Pinky('xx', 2, 'green')
    assert not test_ghost.is_scared
    assert test_ghost.name == 'Pinky'
    assert test_ghost.speed == 2
    assert test_ghost.colour == 'pink'
    test_ghost.speed_up()
    assert test_ghost.speed == 2.2
    assert str(test_ghost)== 'This is pink Pinky, watch out'
    test_ghost.frighten()
    assert test_ghost.colour == 'blue'
    assert test_ghost.is_scared
    assert test_ghost.can_be_eaten()

def test_Inky_Ghost_inheritance_to_all_parrent_class_methods_and_properties():
    test_ghost = Inky('xx', 2, 'green')
    assert not test_ghost.is_scared
    assert test_ghost.name == 'Inky'
    assert test_ghost.speed == 4
    assert test_ghost.colour == 'cyan'
    test_ghost.speed_up()
    test_ghost.speed_up()
    assert test_ghost.speed == 4.84
    assert str(test_ghost)== 'This is cyan Inky, watch out'
    test_ghost.frighten()
    assert test_ghost.colour == 'blue'
    assert test_ghost.is_scared
    assert test_ghost.can_be_eaten()

def test_Clyde_Ghost_inheritance_to_all_parrent_class_methods_and_properties():
    test_ghost = Clyde('xx', 2, 'green')
    assert not test_ghost.is_scared
    assert test_ghost.name == 'Clyde'
    assert test_ghost.speed == 1
    assert test_ghost.colour == 'yellow'
    test_ghost.speed_up()
    assert test_ghost.speed == 1.1
    assert str(test_ghost)== 'This is yellow Clyde, watch out'
    test_ghost.frighten()
    assert test_ghost.colour == 'blue'
    assert test_ghost.is_scared
    assert test_ghost.can_be_eaten()

    