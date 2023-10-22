import pandas as pd
from MusicArchivist import MusicArchivist
from ApiMaster import ApiMaster
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get('COHERE_TOKEN')

api_is_active = True

data_path = '../data/tcc_ceds_music.csv'

archivist = MusicArchivist(data_path)

num = 10000
teste = archivist.get_strings(num)

api = ApiMaster(token, api_is_active)
api = api.connect()

# print(teste)

# query = 'Which music is the best to dance to?'
# results = api.rerank(query, teste, 3)

# print(results)
embeds = []
i = 0
for music_text in teste:
    print(i)
    embeds.append(api.embed(music_text))
    i += 1

output_name = 'database.csv'

df = pd.read_csv(data_path)
df = df.head(num)

em = pd.DataFrame(embeds)

df = df.join(em)

df.to_csv('../data/database.csv')