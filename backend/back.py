from .ApiMaster import ApiMaster
from .MusicArchivist import MusicArchivist
import pandas as pd
import streamlit as st


ENGINEERING = "Answer only with the name of the music as the following example: 'Fur Elise'\nTell me only the name of the music are you being asked to play."


class Back:
    def __init__(self, token: str, data_path):
        self.api = ApiMaster(token, True)
        self.api = self.api.connect()
        self.archivist = MusicArchivist(data_path)

    def classify_instruction(self, s):
        return "break", .69

    def identify_music(self, input: str, engineering: str):
        prompt = f"\"{input}\" \n\n {engineering}"

        return self.api.generate(prompt)

    def prompt_enhancement(self, input: str, engineering: str):
        prompt = f"\"{input}\" \n\n {engineering}"
        
        return self.api.generate(prompt)

    def search_music():
        pass

@st.cache_resource
def get_back(token, data_path):
    return Back(token, data_path)