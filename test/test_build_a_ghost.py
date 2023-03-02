from src.build_a_ghost import (Ghost)

def test_ghost_is_constructed_with_the_appropriate_properties():
    test_ghost = Ghost('Ducky', 3, 'yellow')
    assert test_ghost.name == 'Ducky'
    assert test_ghost.speed == 3
    assert test_ghost.colour == 'yellow'

def test_ghost_is_constructed_with_default_false_is_scared_property():
    test_ghost = Ghost('Ducky', 3, 'yellow')
    assert test_ghost.is_scared is False
    
def test_ghost_can_be_eaten():
    test_ghost = Ghost('Ducky', 6, 'green')
    assert test_ghost.can_be_eaten() is False
    test_ghost.is_scared = True
    assert test_ghost.can_be_eaten() is True

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

    