from .ApiMaster import ApiMaster
from .MusicArchivist import MusicArchivist
import pandas as pd
import streamlit as st

class Back:
    def __init__(self, token: str, data_path):
        self.api = ApiMaster(token, True)
        self.api = self.api.connect()
        self.archivist = MusicArchivist(data_path)

    def classify_instruction(self, s):
        return "break", .69

    def identify_music(self, input: str, enginnering: str):
        prompt = f"\"{input}\" \n\n {enginnering}"

        music_identified = self.api.generate(prompt)
        return music_identified

    def search_music():
        pass

@st.cache_resource
def get_back(token, data_path):
    return Back(token, data_path)