# import modules and assets
import os
from consumables import consumable_items
from weapons import weapons
from players import Player

# set mock player data
player1 = Player(1, [], 15, 1, 2, 10)
player2 = Player(2, [], 18, 2, 5, 25)
player3 = Player(3, [], 13, 4, 1, 8)
player4 = Player(4, [], 16, 1, 3, 17)

def ask_question(prompt):
    # use text input to receive information from user (temporary)
    response = input(f"{prompt} ")
    return response

# speak welcome text
os.system("espeak -g 25 -s 125 'welcome to electronic dungeons and dragons'")

# yes or no input for quickstart guide
os.system("espeak -g 25 -s 125 'would you like to listen to the quickstart guide?'")

quickstart_guide_question = ask_question("would you like to listen to the quickstart guide?")
if quickstart_guide_question == "yes":
    os.system("espeak -g 25 -s 125 -f quickstart.txt")
