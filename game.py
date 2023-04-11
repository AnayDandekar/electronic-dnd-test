# import assets
from voicefunctions import speak_text, ask_question, voice_speed, space_pause_len
from consumables import consumable_items
from players import Player

# set mock player data
player1 = Player(1, [], 15, 10, 2, 1)
player2 = Player(2, [], 18, 25, 5, 2)
player3 = Player(3, [], 13, 8, 1, 4)
player4 = Player(4, [], 16, 17, 3, 1)

# speak welcome text
speak_text("welcome to electronic dungeons and dragons", False, voice_speed, space_pause_len)

# quickstart guide option
speak_text("would you like to listen to the quickstart guide?", False, voice_speed, space_pause_len)
quickstart_guide_question = ask_question("Listen to quickstart guide?")
if quickstart_guide_question == "yes":
    speak_text("quickstart.txt", True, voice_speed, space_pause_len)
