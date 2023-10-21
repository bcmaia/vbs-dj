from ApiMaster import ApiMaster
from MusicArchivist import MusicArchivist
import os
from dotenv import load_dotenv

# Setup
load_dotenv()
api_is_active = True
token = os.environ.get('COHERE_TOKEN')
music_file_path = 'data/test.json'

# Code 
archivist = MusicArchivist(music_file_path)
print(archivist.musics)

api = ApiMaster(token, api_is_active)