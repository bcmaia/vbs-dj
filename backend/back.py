from .ApiMaster import ApiMaster
from .MusicArchivist import MusicArchivist
import pandas as pd
import streamlit as st

class Back:
    def __init__(self, token: str, data_path):
        self.api = ApiMaster(token, True)
        self.archivist = MusicArchivist(data_path)

    # def setup(self):

    
@st.cache_resource
def get_back(token, data_path):
    return Back(token, data_path)