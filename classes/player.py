import random

class Player:
    def __init__(self):
        self.name = ""
        self.ask_name()
        self.nb_doubles = 0
        self.balance = 1500
        self.turns_left_in_jail = 0
        self.position = 0
        self.d1 = 0
        self.d2 = 0
        self.turn = False
        self.properties = []
        
    def ask_name(self):
        self.name = input("Entrez votre nom : ")

    def reset_doubles(self):
        self.nb_doubles = 0

    def throw_dice(self):
        self.d2 = (random.randrange(6)+1)
        self.d1 = (random.randrange(6)+1)

    def throw_dice_for_turn(self):
        self.d2 = (random.randrange(6)+1)
        self.d1 = (random.randrange(6)+1)
        print(self.name,"a obtenu un",str(self.d2),"et un",str(self.d1))
        if self.d1 == self.d2:
            self.nb_doubles+=1
            if self.nb_doubles==3:
                self.turns_left_in_jail = 3
                
    def gain(self, amount): 
        self.balance += amount
    
    def pay_to(self,player, amount):
        if (self.balance-amount) > 0 :
            self.balance -= amount
            player.gain(amount)
            return True
        else:
            return False 
        
    def lose(self, amount):
        if (self.balance-amount) > 0 :
            self.balance -= amount
            return True
        else:
            return False
    
    def move(self):
        self.position +=(self.d1+self.d2)
        if self.position>40:
            self.balance+=200
        self.position = position%40

    def move_to(self, pos):
        self.position = pos


