class Player:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def equals(self, player):
        return self.name == player.name