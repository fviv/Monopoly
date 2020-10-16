class Street(Field):
    def __init__(self,position,name,price,mortgage_price,color,houses_price,rent_by_house):
        super().__init__(position,name,price,mortgage_price,color)
        self.complete_set = False
        self.nb_houses = 0
        self.houses_price = houses_price
        self.rent_by_house = rent_by_house

    def on_landing(self,player):
        super().on_landing()
        if self.owner!= None & self.owner != player:
            if self.complete_set:
                if self.nb_houses == 0:
                    player.pay_to(self.owner,(self.rent_by_house[0]*2))
                else:
                    player.pay_to(self.owner,(self.rent_by_house[self.nb_houses]))

            else:
                player.pay_to(self.owner,self.rent_by_house[0])

    def build_house(self):
        # only if complete set 
        if self.nb_houses<4:
            answer = input("Voulez-vous construire une maison ? y/n")
            if answer=="y":
                self.owner.lose(self.houses_price)
                self.nb_houses+=1

            elif answer == "n":
                pass
            else:
                self.build_house()

        if self.nb_houses==4:
            answer = input("Voulez-vous construire un hotel ? y/n")

    