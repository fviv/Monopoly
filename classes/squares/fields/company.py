from ...player import Player

class Company(Field):
    def __init__(self,position,name,price,mortgage_price,rent,color):
        super().__init__(position,name,price,mortgage_price,rent,color)
        self.complete_set= False


    def on_landing(self,player):
        super().on_landing()
        if self.owner!= None & self.owner != player:
            player.throw_dice()
            if self.complete_set:
                amount=(player.d1 + player.d2)*10
                player.pay_to(self.owner,amount)
            else:
                amount=(player.d1 + player.d2)*4
                player.pay_to(self.owner,amount)
        
    

            
