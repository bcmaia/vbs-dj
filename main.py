import backend
import frontend
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get('COHERE_TOKEN')
data_path = './data/tcc_ceds_music.csv'

back = backend.get_back(token, data_path)
front = frontend.Front()

front.setup(back)
front.run()