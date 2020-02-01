


import itertools, random

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['S','H','D','C']

deck = list(itertools.product(cards,suits))

random.shuffle(deck)

print(deck)

print(len(deck), 'cards')

def draw(deck, num_cards):


    for i in range(num_cards):

        print(deck[0][0], 'of', deck[0][1])
        deck.pop(0)
    
draw(deck, 5)
print(len(deck)) 
