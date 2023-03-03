from src.vectors import (Vector)
import pytest

# test vector only accepts a list of integers 

def test_Vector_raises_TypeError_if_invalid_data_type_is_passed_on():
    with pytest.raises(TypeError, match='Invalid input'):
        Vector(12)
    with pytest.raises(TypeError, match='Invalid input'):
        Vector([1, 2, True])
    with pytest.raises(TypeError, match='Invalid input'):
        Vector([1, 2, [1, 2, 3]])
    with pytest.raises(TypeError, match='Invalid input'):
        Vector([1, 2, 4, {}])

# test it builds vectors appropriately

def test_it_builds_the_vector_attribute_appropriately():
    test_vector =  Vector([12, 3, 4, 5]) 
    assert test_vector.vector  == [12, 3, 4, 5]
    assert test_vector.vector_length == 4

# test vector is_equal method which retruns True if the lengths of both vectors are equal or returns False otherwise

def test_is_equal_method():
    test_vector_1 =  Vector([12, 3, 4, 5]) 
    test_vector_2 =  Vector([6, 33, 71, 2, 4])
    assert test_vector_1.is_equal(test_vector_2) is False
    test_vector_1 =  Vector([12, 3, 4, 5]) 
    test_vector_2 =  Vector([6, 33, 71, 2])
    assert test_vector_1.is_equal(test_vector_2) is True

# test vector add method which adds two vector classes and returns a new vector of the result 

def test_the_functionality_of_add_method_in_Vector_class():
    test_vector_1 = Vector([1, 2, 3])
    test_vector_2 = Vector([1, 2, 3])
    result = test_vector_1.add(test_vector_2)
    assert result.vector == [2, 4, 6]

# test vector subtract method which subract two vector classes and returns a new vector of the result 

def test_the_functionality_of_subtract_method_in_Vector_class():
    test_vector_1 = Vector([1, 2, 3])
    test_vector_2 = Vector([1, 2, 3])
    result = test_vector_1.subtract(test_vector_2)
    assert result.vector == [0, 0, 0]

# test vector dot product method which find the dot product of 2 vectors and returns a new vector of the result 

def test_the_functionality_of_subtract_method_in_Vector_class():
    test_vector_1 = Vector([1, 2, 3])
    test_vector_2 = Vector([2, 3, 4])
    result = test_vector_1.dot_product(test_vector_2)
    assert result == 20

# test vector add, subtract, dot product methods throw an Exception if add is appled to unequal lengths vectors

def test_methods_throw_exception_when_vectors_have_different_lengths():
    test_vector_1 = Vector([1, 2, 3])
    test_vector_2 = Vector([2, 3, 4, 4])
    with pytest.raises(Exception, match='vectors must have same lengths'):
        result = test_vector_1.add(test_vector_2)
    with pytest.raises(Exception, match='vectors must have same lengths'):
        result = test_vector_1.subtract(test_vector_2)
    with pytest.raises(Exception, match='vectors must have same lengths'):
        result = test_vector_1.dot_product(test_vector_2)