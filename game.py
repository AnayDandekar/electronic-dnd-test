import os

#player class
class Player:
    def __init__(self, player_num, inventory):
        self.player_num = player_num
        self.inventory = inventory

# speak welcome text
os.system("espeak \"welcome to electronic dungeons and dragons\"")
