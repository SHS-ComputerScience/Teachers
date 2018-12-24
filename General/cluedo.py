import random

# global variables ----------------------------------------

suspects = ['Colonel Mustard', 
            'Miss Scarlet',
            'Mr Green',
            'Mrs Peacock',
            'Mrs White',
            'Professor Plum']
weapons = ['Candlestick',
           'Dagger',
           'Lead Pipe',
           'Revolver',
           'Rope',
           'Spanner']
rooms = ['Ballroom',
         'Billiard Room',
         'Conservatory',
         'Dining Room',
         'Hall',
         'Kitchen',
         'Library',
         'Lounge',
         'Study']

murder_cards = []
non_murder_cards = []
possible_murder_cards = []
eliminated_murder_cards = []

# subroutines ----------------------------------------------

def populate_possible_murder_cards():
    """ Copy suspect, weapon and room cards to 
    possible_murder_cards list """

    # copy all suspect cards
    for card in suspects:
        possible_murder_cards.append(card)

    # copy all weapon cards
    for card in weapons:
        possible_murder_cards.append(card)

    # copy all room cards   
    for card in rooms:
        possible_murder_cards.append(card)

def populate_murder_cards():
    # select suspect
    max_index = len(suspects) - 1
    random_index = random.randint(0, max_index)
    random_card = suspects[random_index]
    murder_cards.append(random_card)

    # select weapon
    max_index = len(weapons) - 1
    random_index = random.randint(0, max_index)
    random_card = weapons[random_index]
    murder_cards.append(random_card)

    # select room
    max_index = len(rooms) - 1
    random_index = random.randint(0, max_index)
    random_card = rooms[random_index]
    murder_cards.append(random_card)

# main program ---------------------------------------------

# populate possible_murder_cards
# populate murder_cards

# game loop


# tests ------------------------------------------------------

# print('Before:', murder_cards)
# select_murder_cards()
# print('After:', murder_cards)