```python
"""
Huiluo Chen
OOP Program 1
This program will run a card game named The War automatically. The program will simulate detailed
procedures of the game can generate the winner.
Referred Source: http://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
"""

#import necessary class
import os
import random
import time


#Define the ascii card for the game
CARD = """\
┌───────┐
│{}     │
│       │
│   {}  │
│       │
│     {}│
└───────┘
""".format('{trank:^2}', '{suit: <2}', '{brank:^2}')

TEN = """\
┌───────┐
│{}    │
│       │
│   {}  │
│       │
│    {}│
└───────┘
""".format('{trank:^3}', '{suit: <2}', '{brank:^3}')

FACECARD = """\
┌───────┐
│{}│
│       │
│   {}  │
│       │
│{}│
└───────┘
""".format('{trank:<7}', '{suit: <2}', '{brank:>7}')

HIDDEN_CARD = """\
┌───────┐
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
└───────┘
"""

"""
@Class Card
@Description:
    Define the class for creating each single card
@Methods:
    __cmp__(self, other)
    __lt__(self, other) - compare the card rank, override the compare method
"""
class Card(object):
    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace","Hid"]
        #assign different values to each card
        self.card_values = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 11,
            'Queen': 12,
            'King': 13,
            'Ace': 14,  # value of the ace is high until it needs to be low
        }
        #extracting the ascii formatted card
        self.str_values = {
            '2': CARD,
            '3': CARD,
            '4': CARD,
            '5': CARD,
            '6': CARD,
            '7': CARD,
            '8': CARD,
            '9': CARD,
            '10': TEN,
            'Jack': FACECARD,
            'Queen': FACECARD,
            'King': FACECARD,
            'Ace': FACECARD,  # value of the ace is high until it needs to be low
        }
        self.suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs', 'Hid']
        #symbols to be insert into the formatted card
        self.symbols = {
            'Spades': '♠',
            'Diamonds': '♦',
            'Hearts': '♥',
            'Clubs': '♣',
        }
        #convert input into correct type
        if suit == 'Hid':
            #make the hidden hard be able to print horizontally
            self.ascii = self.str_hid()
        else:
            if type(suit) is int:
                self.suit = self.suits[suit]
            else:
                self.suit = suit.capitalize()
            self.rank = str(rank)
            self.symbol = self.symbols[self.suit]
            self.points = self.card_values[str(rank)]
            if self.suit == 'Hid':
                self.ascii = self.str_hid()
            else:
                self.ascii = self.__str__()
    #define the method to print out the object
    def __str__(self):
        symbol = self.symbols[self.suit]
        trank = self.rank + symbol
        brank = symbol + self.rank
        return self.str_values[self.rank].format(trank=trank, suit=symbol, brank=brank)
    #define the method to compare the rank of the card

    def str_hid(self):
        return HIDDEN_CARD

    def __cmp__(self, other):
        return self.ranks.index(self.rank) < self.ranks.index(other.rank)

    def __lt__(self, other):
        return self.__cmp__(other)

"""
@Class Deck
@Description:
    This class represents a deck of cards.
@Methods:
    pop_cards() - removes a card from top of deck
    add_card(card) - adds a card to bottom of deck
    shuffle() - shuffles deck
    sort() - sorts the deck based on value, not suit (could probaly be improved based on need)
"""
class Deck(object):
    def __init__(self):
        # assume top of deck = 0th element
        self.cards = []
        for suit in range(4):
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]:
                self.cards.append(Card(suit, rank))
    #print out the whole deck
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "".join(res)

    def pop_card(self):
        return self.cards.pop(0)

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards = sorted(self.cards)

"""
@Class Player
@Description:
    This class represents player's hand.
@Methods:
    join_lines(self) - print cards in the hand horizontally
    add(self, card) - adds a card into hand
    sort(self) - sort the hand based on card's value
    shuffle(self) - shuffle the hand
    pop_card(self) - pop a card from hand
"""
class Player(list):
    def __init__(self, name ):
        """Initialize the class"""
        super().__init__()
        self.name = name
        self._list = []

    def __len__(self):
        return len(self._list)

    def __str__(self):
        #if the number of cards less than 6, print horizontally.
        if len(self._list) >6:
            res = []
            for card in self._list:
                res.append(str(card))
            return "".join(res)
        else:
            return self.join_lines()

    def join_lines(self):
        liness = [card.ascii.splitlines() for card in self._list]
        return '\n'.join(''.join(lines) for lines in zip(*liness))

    def add(self, card):
        self._list.append(card)

    def sort(self):
        self._list = sorted(self._list)

    def shuffle(self):
        random.shuffle(self._list)

    def pop_card(self):
        return self._list.pop(0)

"""
@Class Game
@Description:
    This class will manage the game.
@Methods:
    distribute (self, hand) - distribute each player 26 cards
    deal(self, hand) - deal a single card from a player's hand and print it
    deal_double(self, hand) - deal two cards and print with one card face down
    join_lines(self, prt) - print cards horizontally
    award(self, hand) - award cards from temp list to winner's hand
"""
class Game(object):
    #initialize the game
    def __init__(self):
        #super().__init__()
        self.deck = Deck()
        self.deck.shuffle()
        #list to temporally store cards played in the round
        self.tight = []
        #define the hidden card
        self.back = Card('Hid', 'Hid')
        #define one of the two time delay
        # ***--------------------Time Delay-------------------------***
        self.delay = 0
        # ***--------------------Time Delay-------------------------***
        #for Windows
        os.system('cls')
        #for Lunix or OS
        #os.system('clear')
        print("**************************************")
        print("Deck is created and the game starts")

    def __str__(self):
        return self.deck.__str__()

    def distribute(self, hand):
        for i in range(26):
            hand.add(self.deck.pop_card())

    def deal(self, hand):
        # pop one card from hand and store one card in show
        show = hand.pop_card()
        self.tight.append(show)
        print("Card dealt by %s" %hand.name)
        print(show)
        time.sleep(self.delay)
        return show

    def deal_double(self, hand):
        #pop two cards from hand and store one card in show
        self.tight.append(hand.pop_card())
        show = hand.pop_card()
        self.tight.append(show)
        #add the hidden card for printting later on
        self.tight.append(self.back)
        prt = self.tight[-2:]
        print("Cards dealt by %s" %hand.name)
        #play one card and the hidden card horizontally
        print(self.join_lines(prt))
        #remove the hidden card from the temp list
        self.tight.pop(-1)
        time.sleep(self.delay)
        return show

    def join_lines(self, prt):
        liness = [card.ascii.splitlines() for card in prt]
        return '\n'.join(''.join(lines) for lines in zip(*liness))

    def award(self, hand):
        for i in range(len(self.tight)):
            hand.add(self.tight.pop())

#create a deck and start the game
Game1 = Game()
#enable player1: Danny
Danny = Player('Danny')
#enable player2: Catherine
Catherine = Player('Catherine')
#distribute 26 cards to each player
Game1.distribute(Danny)
Game1.distribute(Catherine)
#track rounds played in the game
round_count = 0
#time delay during the game
#***--------------------Time Delay-------------------------***
delay = 0
#***--------------------Time Delay-------------------------***
while (1):
    #shuffle each player's hand before each round
    Danny.shuffle()
    Catherine.shuffle()
    time.sleep(delay)
    #check if player has enough cards to play next round
    if Game1.tight:     #if last round is war
        if len(Danny) < 3 and len(Catherine) < 3:
            print("       The game is tie, no winner!")
        elif len(Danny) < 3:
            print("\n       Winner is Catherine!!!\n")
            break
        elif len(Catherine) < 3:
            print("\n       Winner is Danny!!!\n")
            break
    else:               #if last round is not war
        if len(Danny) == 3 and len(Catherine) == 3:
            print("       The game is tie, no winner!")
        elif len(Danny) == 0:
            print("\n       Winner is Catherine!!!\n")
            break
        elif len(Catherine) == 0:
            print("\n       Winner is Danny!!!\n")
            break
    os.system('cls')
    #os.system('clear')
    print(" Right now we have:")
    print(" %s has %r cards in hand now" %(Danny.name, len(Danny)))
    print(" %s has %r cards in hand now\n" %(Catherine.name, len(Catherine)))
    #start the round and deal the card
    if Game1.tight:
        print("****************************************")
        Danny_card = Game1.deal_double(Danny)
        print("****************************************")
        Catherine_card = Game1.deal_double(Catherine)
        print("****************************************")
        #comepare the rank of the card played
        if Danny_card.points > Catherine_card.points:
            print("     %s wins the round\n"  % Danny.name)
            Game1.award(Danny)
        elif Danny_card.points < Catherine_card.points:
            print("     %s wins the round\n" % Catherine.name)
            Game1.award(Catherine)
        else:
            print("  Cards dealt are equal, we have a War!\n")
    else:
        print("****************************************")
        Danny_card = Game1.deal(Danny)
        print("****************************************")
        Catherine_card = Game1.deal(Catherine)
        print("****************************************")
        # comepare the rank of the card played
        if Danny_card.points > Catherine_card.points:
            print("     %s wins the round!!!\n" %Danny.name)
            Game1.award(Danny)
        elif Danny_card.points < Catherine_card.points:
            print("     %s wins the round!!!\n" % Catherine.name)
            Game1.award(Catherine)
        else:
            print("  Cards dealt are equal, we have a War!\n")
    print(" After this round: ")
    print(" %s has %r cards in hand now" %(Danny.name, len(Danny)))
    print(" %s has %r cards in hand now\n" %(Catherine.name, len(Catherine)))
    print(" Temperary list holds %r cards now\n" % (len(Game1.tight)))
    round_count += 1

print("Total rounds played in this game is %s" % round_count)
```
