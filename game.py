# import modules and assets
import os
from consumables import consumable_items
from weapons import weapons
from players import Player

# variables of players
player1 = Player(1, [], 15, 1, 2, 10)
player2 = Player(2, [], 18, 2, 5, 25)
player3 = Player(3, [], 13, 4, 1, 8)
player4 = Player(4, [], 16, 1, 3, 17)

# speak welcome text
os.system("espeak -g 25 -s 125 'welcome to electronic dungeons and dragons. would you like to listen to the quickstart guide?'")

# yes or no input for quickstart guide
answer = input("Quickstart Guide? ")

if answer == "yes":
    os.system("espeak -g 25 -s 125 -f quickstart.txt")
