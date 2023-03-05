

class Ghost:
    is_scared = False

    def __init__(self, name, speed, colour):
        self.name = name
        self.speed = speed
        self.colour = colour

    def __str__(self):
        return f'This is {self.colour} {self.name}, watch out'

    def can_be_eaten(self):
        if self.colour == 'blue':
            self.is_scared == True
        if self.is_scared:
            return True
        else:
            return False

    def frighten(self):
        self.colour = 'blue'
        self.is_scared = True

    def speed_up(self):
        self.speed = round(self.speed * 1.1, 2)


class Blinky(Ghost):
    def __init__(self, name, speed, colour):
        super().__init__(name, speed, colour)
        self.name = 'Blinky'
        self.speed = 3
        self.colour = 'red'


class Pinky(Ghost):
    def __init__(self, name, speed, colour):
        super().__init__(name, speed, colour)
        self.name = 'Pinky'
        self.speed = 2
        self.colour = 'pink'


class Inky(Ghost):
    def __init__(self, name, speed, colour):
        super().__init__(name, speed, colour)
        self.name = 'Inky'
        self.speed = 4
        self.colour = 'cyan'


class Clyde(Ghost):
    def __init__(self, name, speed, colour):
        super().__init__(name, speed, colour)
        self.name = 'Clyde'
        self.speed = 1
        self.colour = 'yellow'
