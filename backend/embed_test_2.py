from ApiMaster import ApiMaster
from MusicArchivist import MusicArchivist
import os
from dotenv import load_dotenv

# def json_to_text(musics):
#     musics_text = []
#     for music in musics:
#         text = ""
#         for field in music:
#             text += (f"{field}: {music[field]}\n")

#     musics_text.append(text)

#     return musics_text

# Setup
load_dotenv()
api_is_active = False
token = os.environ.get('COHERE_TOKEN')
music_file_path = '../data/tcc_ceds_music.csv'

# Code 
# archivist = MusicArchivist(music_file_path)

# music_texts = archivist.get_strings(1)

# print(music_texts)

api = ApiMaster(token, api_is_active)
api = api.connect()

music = api.generate("teste")

print(music)