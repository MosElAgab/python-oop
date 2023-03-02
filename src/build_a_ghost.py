

class Ghost:
    def __init__(self, name, speed, colour):
        self.name = name
        self.speed = speed
        self.colour = colour
        self.is_scared = False

    def can_be_eaten(self):
        if self.is_scared:
            return True
        else:
            return False

    def frighten(self):
        self.colour = 'blue'
        self.is_scared = True

    def speed_up(self):
        self.speed = round(self.speed * 1.1, 2)


    

