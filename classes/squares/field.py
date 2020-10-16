from abc import abstractmethod, ABC
from ..player import Player
from classes.squares.fields.company import Company
from classes.squares.fields.street import Street
from classes.squares.fields.train_station import Train_station
class Field(Square,ABC):
    def __init__(self,position,name,price,mortgage_price, color):
        self.price = price
        self.mortgage_price = mortgage_price
        self.owner = None
        self.mortgage = False
        self.color = color
        super().__init__(position,name)
        
    def collect_rent(self,player):
        player.pay_to(self.owner,self.rent)
    
    def collect_mortgage(self):
        self.owner.gain(self.mortgage_price)
        self.mortgage = True
    
    def buy_back(self):
        self.owner.lose(self.mortgage +(self.mortgage*0.1))
        self.mortgage = False
    
    def buy(self,player):
        if self.owner == None:
            answer = input("Voulez-vous acheter ce terrain ? y/n")
            if answer =="y":
                self.owner = player
                player.lose(self.price)
            elif answer =="n":
                pass
            else:
                self.buy(player)

                

    @abstractmethod
    def on_landing(self,player):
        self.buy(player)
        
