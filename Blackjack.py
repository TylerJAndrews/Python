
import itertools, random

class Deck:

    def __init__(self,):

        self.nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suits = ['Spades','Hearts','Diamonds','Clubs']
        self.cards = list(itertools.product(self.nums,self.suits))
        self.shuffle()

    def shuffle(self,):
        random.shuffle(self.cards)

    def draw(self, num_cards = 1,):
        hand = []

        for i in range(num_cards):
            card = self.cards.pop(0)
            hand.append(card)
            
        return hand


class Blackjack:

    def __init__(self,):

        self.deck = Deck()
        self.score = 0
        self.player_hand = self.deck.draw(2)
        self.update_score()
        self.done = False
        
    def hit(self,):
        '''
            Hit draws a card from the deck and updates score.
            If player has busted, no action is taken.
        '''
        
        if not self.done:
            self.player_hand += self.deck.draw()
            self.update_score()
            self.update_status()

    def stay(self,):
        ''' Player decided to keep hand.'''
        self.done = True

    def update_status(self,):
        ''' Call from hit() or stay() determines if player wants to continue or busted. '''
        
        if self.score > 21 or len(self.player_hand) == 5:
            self.done = True

    def update_score(self,):
        ''' Calculates player's hand score. '''

        score = 0
        num_aces = 0
            
        for card in self.player_hand:

            val = card[0]
            
            if val in ['J', 'Q', 'K']:
                
                score += 10
                
            elif val == 'A':
                
                num_aces += 1
                score += 11
                
            else:
                
                score += int(val)

        # Removes 10 from score equal to number of Aces in hand until score <= 21.
        for aces in range(num_aces):
            if score > 21:
                score -= 10
                
        self.score = score
            
def run_game():

    game = Blackjack()

    while not game.done:
        print(game.player_hand, game.score)
        
        res = input('Press 1 to hit or 2 to stay. ')

        if res == '1':
            game.hit()

        else:
            game.stay()


    print(game.player_hand, game.score)

    if game.score > 21:

        print('You bust!')
        
    print() # Added for formatting
    
    res = input('Would you like to play again? y or n: ')

    if res == 'y':
        print() # Added for formatting
        run_game()

run_game()



