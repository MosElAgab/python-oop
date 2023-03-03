

class Captain:
    
    def __init__(self, name, nickname, crew_size, catchphrase):
        if type(name) is not str or type(nickname) is not str or type(crew_size) is not int or type(catchphrase) is not str:
            raise TypeError('Invalid input')
        self.name = name
        self.nickname = nickname
        self.crew_size = crew_size
        self.catchphrase = catchphrase

class Ship:
    def __init__(self, draft, captain):
        try:
            captain.crew_size
        except AttributeError:
            raise TypeError('Invalid input')
        if type(draft) is not int:
            raise TypeError('Invalid input')
        self.draft = draft
        self.crew = captain.crew_size
    def worth_it(self):
        crew_weight = self.crew * 1.5
        if self.draft - crew_weight >= 20:
            return True
        else:
            return False