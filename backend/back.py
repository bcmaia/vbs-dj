from .ApiMaster import ApiMaster
from .MusicArchivist import MusicArchivist
from .classify import classify as classify 
import pandas as pd
import streamlit as st

class Back:
    def __init__(self, token: str, data_path):
        self.api = ApiMaster(token, True)
        self.archivist = MusicArchivist(data_path)

    def classify_instruction(self, input_string): #receives a string
        return classify(input_string) #returns a string and a float (a command and a confidence)

    def identify_music(self, input: str, engineering: str):
        return self.api.generate(f"\"{input}\" \n\n {engineering}")

    def prompt_enhancement(self, input: str, engineering: str):
        return self.api.generate(f"\"{input}\" \n\n {engineering}")

    def get_moods(self):
        pass

    def get_genres(self):
        pass

    def identify_music(self):
        pass

@st.cache_resource
def get_back(token, data_path):
    return Back(token, data_path)