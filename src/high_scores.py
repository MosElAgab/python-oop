
class HighScoreTable:
    def __init__(self, limit):
        self.scores = []
        self.limit = limit

    def update(self, dict):
        if len(self.scores) < self.limit:          
            self.scores.append(dict)
        else:
            for player in self.scores:
                if dict["score"] > player["score"]:                  
                    self.scores.remove(player)
                    self.scores.append(dict)
            # return "the limit has been reached"

    def average_score(self):
        total = 0
        for player in self.scores:            
            total += player['score']
            
        average = total / self.limit
        return average

    def highest_scorer(self):
        highest = {'player':'Unknown', 'score':0}
        for player in self.scores:
            if player["score"] > highest["score"]:
                highest = player
        return highest

    def reset(self):
        self.scores = []



