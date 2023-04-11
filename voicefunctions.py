# import modules
import os

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
