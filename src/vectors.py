
class Vector:
    def __init__(self, list_of_values):
        if not isinstance(list_of_values, list):
            raise TypeError('Invalid input')
        self.vector = []
        for value in list_of_values:
            if value == True and str(value) != '1':
                raise TypeError('Invalid input')
            elif not isinstance(value, int):
                raise TypeError('Invalid input')
            else:
                self.vector.append(value)
        self.vector_length = len(self.vector)

    def is_equal(self, another_vector):
        if self.vector_length == another_vector.vector_length:
            return True
        else:
            return False

    def add(self, another_vector):
        if not self.is_equal(another_vector):
            raise Exception('vectors must have same lengths')
        result_vector = []
        for i in range(0, self.vector_length):
            result_vector.append(self.vector[i] + another_vector.vector[i])
        return Vector(result_vector)

    def subtract(self, another_vector):
        if not self.is_equal(another_vector):
            raise Exception('vectors must have same lengths')
        result_vector = []
        for i in range(0, self.vector_length):
            result_vector.append(self.vector[i] - another_vector.vector[i])
        return Vector(result_vector)

    def dot_product(self, another_vector):
        if not self.is_equal(another_vector):
            raise Exception('vectors must have same lengths')
        result = 0
        for i in range(0, self.vector_length):
            result += (self.vector[i] * another_vector.vector[i])
        return result