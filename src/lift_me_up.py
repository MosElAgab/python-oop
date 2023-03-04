
class Lift:
    def __init__(self, max_capacity: int or float, floors_count: int or float):
        self.max_capacity = max_capacity
        self.passengers = []
        self.floors_count = floors_count
        self.current_floor = 0
        self.lowest_floor = 0
    
    def find_total_weight(self):
        weight = 0
        for i in range(0, len(self.passengers)):
            weight += self.passengers[i].weight
        return weight

    def add_passenger(self, passenger):
        if (self.max_capacity - self.find_total_weight()) > passenger.weight:
            self.passengers.append(passenger)
    
    def remove_passenger(self, passenger):
        for i in range(0, len(self.passengers)):
            if self.passengers[i] == passenger:
                self.passengers.pop(i)
        return self.find_total_weight()
    
    def move(self, direction):
        directions = ['up', 'down']
        if direction not in [valid_key for valid_key in directions]:
            raise TypeError('Invalid input')
        if direction == 'up':
            if self.current_floor < self.floors_count:
                self.current_floor += 1
            else:
                return 'You are already on the top floor'       
        elif direction == 'down':
            if self.current_floor > self.lowest_floor:
                self.current_floor -= 1
            else:
                return 'You are already on the last floor'

class Passenger:
    def __init__(self, name: str, weight: int or float):
        self.name = name 
        self.weight = weight 
        
    