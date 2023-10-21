import cohere
import json
import os
import numpy as np
from dotenv import load_dotenv

def calc_diff(a, b):
  return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# connect = True
connect = False

load_dotenv()

token = os.environ.get('COHERE_TOKEN')

music_filename = 'raw_music.json'

music = None
with open(music_filename, 'r') as f:
  musics = json.load(f)

musics_text = []
for music in musics:
  text = ""
  for field in music:
    text += (f"{field}: {music[field]}\n")

  musics_text.append(text)

print(musics_text)

if (connect):
  co = cohere.Client(token)
  response = co.embed(musics_text).embeddings

  diff = []
  for i in range(1, len(musics_text)):
    diff.append(calc_diff(response[i - 1], response[i]))

  print(diff)