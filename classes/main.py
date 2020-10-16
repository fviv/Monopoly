from player import Player
class Main : 
    def __init__(self):
        self.nbPlayers = int(input("entrez le nombre de joueurs : "))
        self.players = []
        i=0
        
        while i<self.nbPlayers :
            self.players.append(Player())
            i+=1

        self.turn_orders()
        

    def play_turn(self, player):
        player.throw_dice()
        player.move()
        if player.d1 == player.d2:
            play_turn(player)
    
    def main_loop(self):
        for player in players:
            play_turn(player)

    def turns_order(self):
        playerTurns = []
        for player in self.players:
            player.throw_dice()
        i=0
        while i<len(self.players): 
            if len(playerTurns)>0:
                j=0
                while (1/self.players[i].d1)>(1/playerTurns[j].d1):
                    if j<len(playerTurns):
                        j+=1
                        if j==len(playerTurns):
                            break
                playerTurns.insert(j,self.players[i])  
            else:
                playerTurns.append(self.players[i])
            i+=1
        self.players = playerTurns
