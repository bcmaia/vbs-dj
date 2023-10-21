from ApiMaster import ApiMaster
from MusicArchivist import MusicArchivist
import os
from dotenv import load_dotenv

def json_to_text(musics):
    musics_text = []
    for music in musics:
        text = ""
        for field in music:
            text += (f"{field}: {music[field]}\n")

    musics_text.append(text)

    return musics_text

# Setup
load_dotenv()
api_is_active = False
token = os.environ.get('COHERE_TOKEN')
music_file_path = '../data/musics.json'

# Code 
archivist = MusicArchivist(music_file_path)

music_texts = json_to_text(archivist.musics)

print(music_texts)

api = ApiMaster(token, api_is_active)
api = api.connect()

embbeds = api.embed(music_texts[0])
print(embbeds)