
from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# mycards = [(s,r) for s in SUITE for r in RANKS ]
# list of tupels
# mycards = []

# for s in SUITE : 
#    for r in RANKS:
#        mycards.append((s,r))
#print(mycards)


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Creating a new ordered Deck!")
        self.allcards = [(s,r) for s in SUITE for r in RANKS ] 
        print(self.allcards)

    def shuffle(self):
        print("shuffling Deck")
        shuffle(self.allcards)
    
    def return_in_half(self):
        print("splitting the Deck ...")
        return (self.allcards[:26],self.allcards[26:])

class Hand: 
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))    

    def add_card(self,card):
        self.cards.extend(card)  

    def remove_card(self):
        return self.cards.pop()   


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand 

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    # the matched cards from both players -- war case
    def remove_war_cards(self):
        war_cards = []

        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Returns True if player still has cards
        """
        return len(self.hand.cards) != 0

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!

# create a new deck and split into half
d = Deck()
d.shuffle()
half_1 , half_2 = d.return_in_half()

# create both players
comp = Player("Computer",Hand(half_1))

name = input("what is ur name")
humen = Player(name , Hand(half_2))

total_rounds = 0
war_count = 0

while humen.still_has_cards() and comp.still_has_cards():
    total_rounds +=1
    print("Time for a new round")
    print("here are the current standings")
    print("{} has the count {}".format(comp.name,len(comp.hand.cards)))
    print("{} has the count {}".format(humen.name,len(humen.hand.cards)))
    print("play a card")
    print("\n")

    # represent the cards on the table 
    table_cards = []

    c_cards = comp.play_card()
    h_cards = humen.play_card()

    table_cards.append(c_cards)
    table_cards.append(h_cards)

    # print("c_cards[1]"+str(c_cards[1]))
    
    # if war case (matched card)
    if c_cards[1] == h_cards[1]:
        war_count +=1
        print("######It's War#######")
        print("We have a match, time for war!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        
        table_cards.extend(humen.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        
        # print("index(c_cards[1]"+ str(RANKS.index(c_cards[1])))
        # print("RANKS.index(c_cards[1])"+ str(RANKS.index(c_cards[1])))
        # Check to see who had higher rank

        #  The index() method finds the first occurrence of the specified value.
        #  The index() method raises an exception if the value is not found.
       
        # here extracting c_cards[1] index according to RANKS

        if RANKS.index(c_cards[1]) < RANKS.index(h_cards[1]) :
            print(humen.name+" has the higher card, adding to hand.")
            humen.hand.add_card(table_cards)
       
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add_card(table_cards)

    # continue the procedure
    else :         
        if RANKS.index(c_cards[1]) < RANKS.index(h_cards[1]) :
            print(humen.name+" has the higher card, adding to hand.")
            humen.hand.add_card(table_cards)
       
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add_card(table_cards)

print("game over , number of rounds {}".format(total_rounds))
print("a war happend {} times".format(war_count))