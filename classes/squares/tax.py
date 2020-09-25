from ..player import Player
class Tax:
    def __init__(self,name,price):
        self.name = "impot sur"+name
        self.price = price
    
    def on_landing(self,player):
        player.lose(price)
    
