

class user:

    def __init__(self):
        self.current_balance = float(0)
        self.pots = {}

    def deposit_money(self, amount):
        self.current_balance += amount

    def create_new_pot(self, pot_name):
        if type(pot_name) is not str:
            raise TypeError('Invalid input')
        self.pots[pot_name] = {'pot_balance': float(0)}

    def add_to_pot(self, pot_name, amount):
        available_pots = [key for key in self.pots]
        if pot_name not in available_pots:
            raise Exception('there is no money pot with this name')
        self.pots[pot_name]['pot_balance'] += amount

    def transfer_to_pot(self, pot_name, amount):
        if amount < self.current_balance:
            self.pots[pot_name]['pot_balance']+= amount
            self.current_balance -= amount
        else:
            print('insufficient funds')