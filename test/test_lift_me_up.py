from src.lift_me_up import (Lift, Passenger)
import pytest

def test_Lift_class_holds_the_appropriate_propeties():
    new_lift = Lift(100, 5)
    assert new_lift.max_capacity == 100
    assert new_lift.passengers == []
    assert new_lift.floors_count == 5
    assert new_lift.current_floor == 0

def test_Passenger_Class_holds_the_appropriate_properties():
    ali = Passenger('ali', 46)
    assert ali.name == 'ali'
    assert ali.weight == 46

def test_the_functionality_of_add_passenger_method_and_find_total_weight_method_in_the_Lift_class():
    new_lift = Lift(160, 5)
    ali = Passenger('ali', 46)
    new_lift.add_passenger(ali)
    assert new_lift.passengers == [ali]
    alex = Passenger('alex', 96)
    new_lift.add_passenger(alex)
    assert new_lift.passengers == [ali, alex]
    assert new_lift.find_total_weight() == 142
    omar = Passenger('omar', 50)
    new_lift.add_passenger(omar)
    assert new_lift.find_total_weight() == 142
    assert new_lift.passengers == [ali, alex]


def test_the_functionality_of_remove_passenger_method_in_the_Lift_class():
    new_lift = Lift(160, 5)
    ali = Passenger('ali', 46)
    new_lift.add_passenger(ali)
    alex = Passenger('alex', 96)
    new_lift.add_passenger(alex)
    omar = Passenger('omar', 70)
    new_lift.add_passenger(omar)
    assert new_lift.remove_passenger(alex) == 46
    assert new_lift.passengers == [ali]
    assert new_lift.find_total_weight() == 46
    new_lift.add_passenger(omar) == 116
    assert new_lift.find_total_weight() == 116
    assert new_lift.passengers == [ali, omar]

def test_the_functionality_of_move_method_in_the_Lift_class():
    new_lift = Lift(200, 5)
    ali = Passenger('ali', 46)
    new_lift.add_passenger(ali)
    new_lift.move('up')
    assert new_lift.current_floor == 1
    new_lift.move('up')
    new_lift.move('up')
    new_lift.move('down')
    assert new_lift.current_floor == 2
    new_lift.move('up')
    new_lift.move('up')
    new_lift.move('up')
    new_lift.move('up')
    assert new_lift.current_floor == 5



