import random

# global constants ----------------------------------------

SUSPECTS = ['Colonel Mustard', 
            'Miss Scarlet',
            'Mr Green',
            'Mrs Peacock',
            'Mrs White',
            'Professor Plum']

WEAPONS = ['Candlestick',
           'Dagger',
           'Lead Pipe',
           'Revolver',
           'Rope',
           'Spanner']
           
ROOMS = ['Ballroom',
         'Billiard Room',
         'Conservatory',
         'Dining Room',
         'Hall',
         'Kitchen',
         'Library',
         'Lounge',
         'Study']

# global variables ----------------------------------------

actual_murder_cards = []
remaining_murder_cards = []
possible_murder_cards = []
eliminated_murder_cards = []
suspected_murder_cards = []
turn_counter = 0

# subroutines ---------------------------------------------

def set_possible_murder_cards():
    """ Copy all cards to possible_murder_cards list """

    # copy suspect cards
    for card in SUSPECTS:
        possible_murder_cards.append(card)

    # copy weapon cards
    for card in WEAPONS:
        possible_murder_cards.append(card)

    # copy room cards
    for card in ROOMS:
        possible_murder_cards.append(card)
    

def select_actual_murder_cards():
    """ Copy random suspect, weapon & room card to envelope list """

    # random suspect card
    max_index = len(SUSPECTS) - 1
    random_index = random.randint(0, max_index)
    random_card = SUSPECTS[random_index]
    envelope.append(random_card)

    # random weapon card
    max_index = len(WEAPONS) - 1
    random_index = random.randint(0, max_index)
    random_card = WEAPONS[random_index]
    envelope.append(random_card)

    # random room card
    max_index = len(ROOMS) - 1
    random_index = random.randint(0, max_index)
    random_card = ROOMS[random_index]
    envelope.append(random_card)


def deal_cards(n):
    """ Move n cards from possible_murder_cards list to 
    eliminated_murder_cards list """
    
    for i in range(n):
        max_index = len(possible_murder_cards) - 1
        random_index = random.randint(0, max_index)
        random_card = possible_murder_cards.pop(random_index)
        eliminated_murder_cards.append(random_card)


def ask_to_see_cards():

    # pick 3 random cards from possible_murder_cards list
    # and compare with remaining_murder_cards list. If they
    # are present, move from possible_murder_cards list to
    # eliminated_murder_cards list, else they are the actual
    # murder cards in the envelope list



# main program --------------------------------------------

select_actual_murder_cards()
set_possible_murder_cards()
deal_cards(3)

# game loop -----------------------------------------------

# ask_to_see_cards()

# tests ---------------------------------------------------

