import backend
import frontend
import os
from dotenv import load_dotenv

# Setup
load_dotenv()
token = os.environ.get('COHERE_TOKEN')
data_path = './data/tcc_ceds_music.csv'

# Initialize the backend and frontend
back = backend.get_back(token, data_path)
front = frontend.Front()

# Run frontend
front.setup(back)
front.run()