from ..player import Player
class Field(Square):
    def __init__(self,price,mortgage_price,rent):
        self.price = price
        self.mortgage_price = mortgage_price
        self.rent = rent
        self.owner 
        self.mortgage = False
        
    def collect_rent(self,player):
        player.pay_to(self.owner,self.rent)
    
    def collect_mortgage(self):
        self.owner.gain(mortgage_price)
        self.mortgage = True
    
    def buy_back(self):
        self.owner.