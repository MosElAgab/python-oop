# make sure to import and install pytest
# make sure to import your class
from src.coder import (coder)


def test_coder_instance_has_the_correct_constructor_attributes():
    result = coder('Alex', 'stockport', 'Software Engineering', 'March 2020')
    print(f'result => {result}')
    assert result.name == 'Alex'
    assert result.location == 'stockport'
    assert result.course == 'Software Engineering'
    assert result.graduation_date == 'March 2020'


def test_returns_a_greeting():
    expected = 'Hello Joe, my name is Alex'
    alex = coder('Alex', 'stockport', 'Software Engineering', 'March 2020')
    result = alex.greeting('Joe')
    print(f'result => {result}')
    assert expected == result


def test_alumni_():
    # this test is valid before October
    expected = False
    alex = coder('Alex', 'stockport', 'Software Engineering', 'October 2023')
    result = alex.alumni()
    print(f'result => {result}')
    assert expected == result

    expected = True
    alex = coder('Alex', 'stockport', 'Software Engineering', 'January 2023')
    result = alex.alumni()
    print(f'result => {result}')
    assert expected == result

    expected = True
    alex = coder('Alex', 'stockport', 'Software Engineering', 'May 2014')
    result = alex.alumni()
    print(f'result => {result}')
    assert expected == result
