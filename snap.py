from cards import *

class Player(Deck):
    def __init__(self,name,id):
        super().__init__()
        self.name = name
        self.id = id
    
class SnapGame():
    """a game of snap use 'turn' method to play a turn and the 'try_snap' method"""
    def __init__(self,number_of_players):
        self.center_pile = Deck().init_standard(no_jokers=True).shuffle()
        self.players = []
        for i in range(number_of_players):
            self.players.append(Player(f"player {i}",i))
        self.center_pile.deal(self.players)

        self.__turn_num = 0
    @property
    def player_of_current_turn(self):
        """returns the the player whos turn it is"""
        return self.players[self.__turn_num%self.number_of_players]
    @property
    def number_of_players(self):
        return len(self.players)
    def turn(self):
        """take the turn of the next player in the rotation"""
        if len(self.players) == 1:
                return self.players[0]
        player_of_turn = self.players[self.__turn_num%self.number_of_players]
        player_of_turn.move_top(self.center_pile)
        if player_of_turn.number_of_cards == 0:
            self.players.remove(player_of_turn)
        self.__turn_num += 1

    def try_snap(self,player_indexs):
        temp_pile = self.center_pile.cards
        if len(temp_pile) > 1:
            if temp_pile[-1].value == temp_pile[-2].value:
                self.players[player_indexs].merge_bottom(self.center_pile)
                return True
            else:
                return False
