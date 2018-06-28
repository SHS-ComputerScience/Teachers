import random


class Card():

    _RANKS = [{'text': 'Ace', 'symbol': 'A'},
              {'text': 'Two', 'symbol': '2'},
              {'text': 'Three', 'symbol': '3'},
              {'text': 'Four', 'symbol': '4'},
              {'text': 'Five', 'symbol': '5'},
              {'text': 'Six', 'symbol': '6'},
              {'text': 'Seven', 'symbol': '7'},
              {'text': 'Eight', 'symbol': '8'},
              {'text': 'Nine', 'symbol': '9'},
              {'text': 'Ten', 'symbol': '10'},
              {'text': 'Jack', 'symbol': 'J'},
              {'text': 'Queen', 'symbol': 'Q'},
              {'text': 'King', 'symbol': 'K'}]
    _SUITS = [{'text': 'Spades', 'symbol': '♠'},
              {'text': 'Hearts', 'symbol': '♥'},
              {'text': 'Clubs', 'symbol': '♣'},
              {'text': 'Diamonds', 'symbol': '♦'}]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self._set_image()

    def __repr__(self):
        return self._RANKS[self.rank]['text'] + ' of ' + self._SUITS[self.suit]['text']

    def _set_image(self):
        if self.rank == 9: pad = 4
        else: pad = 5
        self._image = ['╔═══════╗',
                       '║ {0}{1}║'.format(self._RANKS[self.rank]['symbol'], ' ' * pad),
                       '║   {}   ║'.format(self._SUITS[self.suit]['symbol']),
                       '║{1}{0} ║'.format(self._RANKS[self.rank]['symbol'], ' ' * pad),
                       '╚═══════╝']

    def get_image(self):
        return self._image
    

class Deck():
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in range(4) for rank in range(13)]
        self.n_cards = len(self.cards)

    def shuffle(self):
        for i in range(3):
            random.shuffle(self.cards)
    
    def _deal_card(self, player):
        player.hand.append(self.cards.pop())
        self.n_cards -= 1
    
    def deal_cards(self, players, n_cards):
        for i in range(n_cards):
            for player in players:
                if self.n_cards <= 0:
                    break
                self._deal_card(player)

    # def print_deck(self):
    #     for card in self.cards:
    #         print(card)


class Hand(Deck):
    def __init__(self):
        super().__init__()
        self.cards = []

    def display(self):
        if self.n_cards > 0:
            lines = len(self.cards[0])
            for line in range(lines):
                for card in self.cards:
                    print(card[line], end=' ')
                print()

class Player():
    hand = Hand()

    def __init__(self, name):
        self.name = name

    def show_hand(self):
        for card in self.hand:
            print(card.name)



deck = Deck()
players = [Player('Player 1'), Player('Player 2')]

deck.shuffle
deck.deal_cards(players, deck.n_cards)

players[0].hand.display()

# repeat until 1 player has no cards
#     player 1 puts card down
#     player 2 puts card down
#     check if card ranks match
#     if true, work out which player says snap
#         that player gets point and cards
#         repeat
#     if false
#         repeat