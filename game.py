# import modules
import os
# import assets
from consumables import consumable_items
from weapons import weapons
from players import Player

# set players
player1 = Player(1, [], 15, 1, 2)
player2 = Player(2, [], 18, 2, 5)
player3 = Player(3, [], 13, 4, 1)
player4 = Player(4, [], 16, 1, 3)

# speak welcome text
os.system("espeak 'welcome to electronic dungeons and dragons'")
