import pandas as pd
from MusicArchivist import MusicArchivist
from ApiMaster import ApiMaster
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get('COHERE_TOKEN')

api_is_active = True

music_file_path = '../data/tcc_ceds_music.csv'

archivist = MusicArchivist(music_file_path)

num = 1000
teste = archivist.get_strings(num)

api = ApiMaster(token, api_is_active)
api = api.connect()

embbeds = []
i = 0
for music_text in teste:
    print(i)
    embbeds.append(api.embed(music_text))
    i += 1

output_name = 'database.csv'

df = pd.read_csv(music_file_path)
df = df.head(num)

em = pd.DataFrame(embbeds)

df = df.join(em)

df.to_csv('../data/database.csv')