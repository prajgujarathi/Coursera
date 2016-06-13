# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
massage= ""
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    def drawBack(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, 
                          [pos[0] + CARD_BACK_CENTER[0], 
                           pos[1] + CARD_BACK_CENTER[1]], 
                          CARD_BACK_SIZE)
# define hand class
class Hand:
    def __init__(self):
        self.card_list = []

    def __str__(self):
        result = ""
        for card in self.card_list:
            result += " " + str(card)
        return "Hands Contain: "+result    

    def add_card(self, card):
        self.card_list.append(card)

    def get_value(self):
        Value = 0
        has_an_Ace = False
        for card in self.card_list:
            rank = card.rank
            Value += VALUES[rank]
            if rank == 'A':
                has_an_Ace = True
        if (has_an_Ace and Value < 11):
            Value += 10
        return Value
   
    def draw(self, canvas, pos):
        for card in self.card_list:
            card.draw(canvas, pos)
            pos[0] = pos[0] + 80
            
# define deck class 
class Deck:
    def __init__(self):
        self.deck_cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck_cards)

    def deal_card(self):
        return self.deck_cards.pop(0)
    
    def __str__(self):
        result = ""
        for card in self.deck_cards:
            result += " " + card.__str__()
        return "Deck Contain: "+ result    



#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, Deck_of_Cards ,score ,massage
    outcome = ""
    massage= ""
    if(in_play == True):
        outcome = "Player lost because of re-deal! New Game?"
        score -= 1
        in_play = False
    else:    
        in_play = True
        Deck_of_Cards = Deck()
        Deck_of_Cards.shuffle()
        player = Hand()
        dealer = Hand()
        player.add_card(Deck_of_Cards.deal_card())
        player.add_card(Deck_of_Cards.deal_card())
        dealer.add_card(Deck_of_Cards.deal_card())
        dealer.add_card(Deck_of_Cards.deal_card())
        
    print player
    print dealer

def hit():
    global massage, score, outcome, in_play, player, dealer, Deck_of_Cards
    if(player.get_value() < 21):
        player.add_card(Deck_of_Cards.deal_card())
        print player.get_value()
    if(player.get_value() > 21):
        massage = "You are Busted"
        score -= 1
        in_play = False
        outcome = "New Game?"
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global massage, score,outcome, in_play, player, dealer, Deck_of_Cards
    if in_play:
            while(dealer.get_value() < 17 ):
                dealer.add_card(Deck_of_Cards.deal_card())
                print dealer.get_value()
            if(dealer.get_value() < player.get_value()):
                massage = "Congradulation!! You Won!"
                score += 1
                outcome = "New Game?"
                in_play = False
                print massage
            elif(dealer.get_value() > 21):
                massage = "Dealer is Busted..You Won!!"
                score += 1
                outcome = "New Game?"
                print massage
                in_play = False
            else: 
                massage = "Dealer Won!!"
                score -= 1
                outcome = "New Game?"
                print massage
                in_play = False
            
        
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BlackJack",(225,50),50,"White")
    canvas.draw_text("Hit or Stand?",(50,150),20,"Black")
    canvas.draw_text(outcome, (200, 355), 20, "Black")
    canvas.draw_text(massage, (200, 155), 20, "Black")
    canvas.draw_text("Dealer", (100, 185), 20, "Blue")
    canvas.draw_text("Player", (100, 385), 20, "Blue")
    Score = canvas.draw_text("Score: " + str(score), (450, 100), 30, "Black")
    dealer.draw(canvas, [100, 200])
    player.draw(canvas, [100, 400])
    if in_play:
        dealer.card_list[0].drawBack(canvas, [100, 199])
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
