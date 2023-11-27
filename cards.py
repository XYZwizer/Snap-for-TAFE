import random

class Card:
    all_suites = ["SPADE","HEART","DIAMOND","CLUB"]
    all_value = ["ACE","2","3","4","5","6","7","8","9","JACK","QUEEN","KING","JOKER"]

    def __init__(self,value:str,suite:str):
        self.value = value
        self.suite = suite
    def __repr__(self) -> str:
        return self.value + "♠♥♦♣"[Card.all_suites.index(self.suite)]
    def unicode_char(self) -> chr:
        if self.value == "JOKER":
            if self.suite == "HEART" or self.suite == "DIAMOND":
                return "🂿"
            else:
                return "🃏"
        card_val = 0x1F000
        suites_val = [0xA0,0xB0,0xC0,0xD0][Card.all_suites.index(self.suite)]
        value_val = [1,2,3,4,5,6,7,8,9,0xB,0xD,0xE,0xF][Card.all_value.index(self.value)]
        return chr(card_val+suites_val+value_val)

class Deck:
    def __init__(self):
        self.__cards = []
    def __repr__(self) -> str:
        return str(self.__cards)
    @property
    def cards(self):
        return self.__cards.copy()   
    @property
    def number_of_cards(self):
        return len(self.__cards)

    def __getitem__(self, item):
        return self.__cards[item]

    def __iter__(self):
        self.__iternum = -1;
        self.__itersize = len(self.__cards);
        return self
    def __next__(self):
        self.__iternum += 1
        if self.__iternum < self.__itersize:
            return self.__cards[self.__iternum]
        else:
            raise StopIteration

    def init_standard(self,no_jokers=False):
        for suite in Card.all_suites:
            for value in Card.all_value:
                if not (value == "JOKER" and no_jokers):
                    self.__cards.append(Card(value,suite))
        return self
    def append(self,new_card):
        self.__cards.append(new_card)
    def shuffle(self):
        random.shuffle(self.__cards)
        return self
    def move_top(self,reciver):
        reciver.append(self.__cards.pop())

    def clear(self):
        self.__cards = []
    def merge_bottom(self,takeing_from):
        self.__cards =  self.__cards + takeing_from.cards
        takeing_from.clear()
    def deal(self,hands):
        number_of_hands = len(hands)
        hand_to_give_to = 0
        while(len(self.__cards) != 0):
            self.move_top(hands[hand_to_give_to])
            hand_to_give_to += 1 
            hand_to_give_to = hand_to_give_to % (number_of_hands)