# import modules and assets
import os
from consumables import consumable_items
from weapons import weapons
from players import Player

# default text to speech settings
voice_speed = 120
space_pause_len = 10

# set mock player data
player1 = Player(1, [], 15, 1, 2, 10)
player2 = Player(2, [], 18, 2, 5, 25)
player3 = Player(3, [], 13, 4, 1, 8)
player4 = Player(4, [], 16, 1, 3, 17)

def speak_text(text, is_file, voice_speed, space_pause_len):
    # speak text with settings from function parameters
    if not is_file:
        os.system(f"espeak -s {voice_speed} -g {space_pause_len} '{text}'")
    # speak file with settings from function parameters
    if is_file:
        os.system(f"espeak -s {voice_speed} -g {space_pause_len} -f {text}")

def ask_question(prompt):
    # use text input to receive information from user (temporary)
    response = input(f"{prompt} ")
    return response

# speak welcome text
speak_text("welcome to electronic dungeons and dragons", False, voice_speed, space_pause_len)

# quickstart guide option
speak_text("would you like to listen to the quickstart guide?", False, voice_speed, space_pause_len)
quickstart_guide_question = ask_question("Listen to quickstart guide?")
if quickstart_guide_question == "yes":
    speak_text("quickstart.txt", True, voice_speed, space_pause_len)
