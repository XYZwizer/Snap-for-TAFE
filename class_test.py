from snap import *

#random.seed(102434654)

game = SnapGame(2)

while True:
    winner = game.turn()
    if winner:
        print("winner",winner.name)
        break
    randdddd = random.randint(0,len(game.players)-1)
    game.try_snap(randdddd)
    
