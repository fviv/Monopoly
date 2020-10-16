class Train_station(Field):
    def __init__(self,position,name,price,mortgage_price,color):
        super().__init__(position,name,price,mortgage_price,color)
        self.nb_trains = 0

    def on_landing(self,player):
        super().on_landing()
        if self.owner!= None & self.owner != player:
            if self.nb_trains == 1:
                player.pay_to(self.owner,25)

            if self.nb_trains == 2:
                player.pay_to(self.owner,50)

            if self.nb_trains == 3:
                player.pay_to(self.owner,100)

            if self.nb_trains == 4:
                player.pay_to(self.owner,200)
    


            
        
    