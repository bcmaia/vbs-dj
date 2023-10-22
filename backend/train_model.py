import cohere
import csv
import os
from cohere.custom_model_dataset import CsvDataset  
from dotenv import load_dotenv

#pip install dotenv
#pip install cohere

# Setup
load_dotenv()
api_is_active = False
token = os.environ.get('COHERE_TOKEN')



dataset = CsvDataset(train_file="backend/classify_examples.csv", delimiter=",")  

co = cohere.Client(token)
fintun = co.create_custom_model(name="papagaio_classify_2",model_type='CLASSIFY',dataset=dataset)
print(fintun)