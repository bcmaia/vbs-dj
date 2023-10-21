import cohere
import json
import os
from dotenv import load_dotenv

connect = False

load_dotenv()

token = os.environ.get('COHERE_TOKEN')

music = None
music_filename = 'test.json'

with open(music_filename, 'r') as f:
  music = json.load(f)

print(token)

if (connect):
  co = cohere.Client(token)

print(music)

# response = co.embed(
#   texts=[str(music)],
#   model='small',
# )

# print(response)
