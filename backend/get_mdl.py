import cohere
import os
from dotenv import load_dotenv

load_dotenv()
api_is_active = False
token = os.environ.get('COHERE_TOKEN')
co = cohere.Client(token)

lcm = cohere.Client.list_custom_models(co)
print(lcm)
print(lcm[0])
print(lcm[1])