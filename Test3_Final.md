```python
'''
Object&Oriental Programing Take Home Final
Huiluo Chen
Due: 10th May
Description: This program simulates the Roulette Wheel game.
'''

# import necessary library
import random
import os
import time

'''
@Class roulette_wheel
@Description:
    Define the class for the wheel
@Methods:
    spin: spin the wheel and return a number with color
'''
class roulette_wheel(object):
    def __init__(self):
        self.wheel = {'green':[0, "00"], 'black':[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35],
                      'red':[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]}

    def spin(self):
        result = {}
        number = random.randint(0,37)
        if number == 37:                # 37 represents '00' on the roulette wheel
          number = '00'
        for k, v in self.wheel.items(): # define the color from the wheel dictionary
          if number in v:
              color = k
        result["number"] = number
        result["color"] = color
        return result

'''@Class roulette_table
@Description:
    Define the class for the payout table of the roulette wheel
@Methods:
    payout: find corresponding payout through the player's bet and return it
'''

class roulette_table(object):
    def __init__(self):
        self.bet_payout = {35:["straight"],17:["split"],11:["street"],8:["corner"],
                           2:["c1","c2","c3","d1","d2","d3"],1:["even","odd","red","black","1-18","19-36"]}
        self.comb = {"c1":[1,4,7,10,13,16,19,22,25,28,31,34],"c2":[2,5,8,11,14,17,20,23,26,29,32,35],
                     "c3":[3,6,9,12,15,18,21,24,27,30,33,36],"d1":[1,2,3,4,5,6,7,8,9,10,11,12],
                     "d2":[13,14,15,16,17,18,19,20,21,22,23,24],"d3":[25,26,27,28,29,30,31,32,33,34,35,36],
                     "even":[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36],
                     "odd":[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35],
                     "red":[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36],
                     "black": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
                     "1-18":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
                     "19-36":[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]}
        # Used to check if the user input is the correct type
        self.bet_type = ["straight", "split", "street", "corner", "c1","c2","c3","d1","d2","d3",
                         "even", "odd", "red", "black", "1-18", "19-36"]

    def payout(self, bet):
        for k, v in self.bet_payout.items():
            if bet[0] in v:             #check what type of bet the player made
                payout = k
        return payout

'''@Class player
@Description:
    Define the class for a single player to record necessary informations
@Methods:
    makebet: assign user input into the player's info
'''

class player(object):
    def __init__(self, name = None, total_bank = 0, bet_amount = 0, bet = None):
        self.name = name
        self.total_bank = total_bank
        self.current_bet_amount = bet_amount
        self.current_bet = bet  #The player's bet is the list contains the numbers or sections been bet

    def makebet(self, bet_amount = 0, bet=None):
        self.current_bet_amount = bet_amount
        self. current_bet = bet

'''@Class game
@Description:
    Define the class to handle and excute the roulette whell game
@Methods:
    game_play: spin the wheel and determine player's total bank change based on the player's bet
    game_start: handle the progress of the game.
'''

class game(object):
    def __init__(self, name = None, total_bank = 0):
        # Create three instance of previously defined class
        self.current_player = player(name, total_bank)
        self.current_wheel = roulette_wheel()
        self.table = roulette_table()

    def game_play(self):
        # spin the wheel and get the result
        result = self.current_wheel.spin()
        # determine the payout based on player's bet
        payout = self.table.payout(self.current_player.current_bet)
        print("The spin result is",result["number"], "in",result["color"])
        
        # check if player bet with any numbers directly
        if result["number"] in self.current_player.current_bet:
            self.current_player.total_bank += payout*self.current_player.current_bet_amount
            print("You win the round and your total bank now is", self.current_player.total_bank)
            
        # if no numbers present in player's bet, check if the bet type wins
        elif self.current_player.current_bet[0] in self.table.comb:
            if result["number"] in self.table.comb[self.current_player.current_bet[0]]:
                self.current_player.total_bank += payout*self.current_player.current_bet_amount
                print("You win the round and your total bank now is", self.current_player.total_bank)
            else:
                # Remove the bet amount from the total bank
                self.current_player.total_bank += -self.current_player.current_bet_amount
                print("You lose the round and your total bank now is", self.current_player.total_bank)
                
        # Remove the bet amount from the total bank
        else:
            self.current_player.total_bank += -self.current_player.current_bet_amount
            print("You lose the round and your total bank now is", self.current_player.total_bank)

    def game_start(self):
        round = 1       # record how many rounds been played
        # check if the remaining balance is 0 or reaches the winning amount
        while (game1.current_player.total_bank > 0 or game1.current_player.total_bank >= 10000):
            print("Now is round", round)
            print(game1.current_player.name, "current total bank:", game1.current_player.total_bank)
            '''
            For the bet format, please start with bet type, and the numbers related to your bet type if applicable.
            Examples: "straight 00", "split 23 14" or "even"
            '''
            # Process user input and generate the bet list
            raw_bet = input("Please input your bet: ").split()
            bet = []
            bet.append(raw_bet[0])
            raw_bet.pop(0)
            for x in raw_bet:
                if x == '00':
                    bet.append(x)
                else:
                    bet.append(int(x))
            # get the bet amount from user
            bet_amount = int(input("Please input your bet amount: "))
            # check if the bet type is correct
            if bet[0] not in game1.table.bet_type:
                print("Wrong bet type")
                time.sleep(2)
                os.system('clear')
            # check if the balance is sufficient
            elif bet_amount > game1.current_player.total_bank:
                print("Invalid bet: exceeding the total bank")
                time.sleep(2)
                os.system('clear')
            # excute the game if passed the two check points
            else:
                # assign the the bet and bet_amount to the player class
                game1.current_player.makebet(bet_amount, bet)
                print("Your bet is", game1.current_player.current_bet)
                print("Start to rotate the Roulette Wheel")
                # spin the wheel and determine if player win or lose
                game1.game_play()
                round += 1
                time.sleep(5)
                os.system('clear')
        print("The game is over and your total bank is", game1.current_player.total_bank)

# initialize the game with player's name and initial total bank amount.
game1 = game("Danny", 5000)
game1.game_start()
```
