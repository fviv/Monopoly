from player import Player
class Main : 
    def __init__(self):
        self.nbPlayers = input("entrez le nombre de joueurs : ")
        self.players = []
        i=0
        while i<nbPlayers :
            self.players[i] = Player()
            i+=1

    def play_turn(self, player):
        player.throw_dice()
        player.move()
        if player.d1 == player.d2:
            play_turn(player)
    
    def main_loop(self):
        for player in players:
            play_turn(player)

