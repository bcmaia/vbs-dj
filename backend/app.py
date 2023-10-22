from ApiMaster import ApiMaster
from cohere.responses.classify import Example
from MusicArchivist import MusicArchivist
from dotenv import load_dotenv
import os

# Setup
load_dotenv()
api_is_active = False
token = os.environ.get('COHERE_TOKEN')
music_file_path = '../data/musics.json'

print("O que precisa hoje?")

known_commands = {
    "stop": 0,
    "play": 1,
    "find": 2,
}


examples = [
    Example("Please, play", "play"),
    Example("Hit it", "play"),
    Example("Stop now", "stop"),
    Example("You can stop", "stop"),
    Example("Could you show me", "find"),
    Example("List this", "find"),
    Example("Search for your mom", "find"),
    Example("I want sonata", "play"),
    Example("Can I see", "find"),
    Example("One moment", "stop")
]

while True:
    user_text = input()
    user_text = user_text.split(' ', maxsplit=1)
    command_text = user_text[0]
    command_text = command_text.lower()
    music = None

    if (command_text in known_commands):
        command = known_commands[command_text]
        match(command):
            case 0:
                music = None
                print("No music is playing.")

            case 1:
                music = user_text[1]
                print(f"Now playing {music}.")

            case 2:
                if (music != None):
                    print(f"Currently playing {music}.")
                else:
                    print("No music is currently playing.")
                
            case 3:
                print(f"Searching for musics similar to {user_input[1]}")

            case -1:
                break
    
    else:
        print(f"Unknown command: {command_text}")