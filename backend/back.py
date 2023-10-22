from .ApiMaster import ApiMaster
from .MusicArchivist import MusicArchivist
from .classify import classify as classify
import pandas as pd
import streamlit as st



ENGENEERING = "Answer only with the name of the music as the following example: 'Fur Elise'\nTell me only the name of the music are you being asked to play."


class Back:
    def __init__(self, token: str, data_path):
        self.api = ApiMaster(token, True).connect()
        self.archivist = MusicArchivist(data_path)

    def classify_instruction(self, input_string):  # receives a string
        return classify(
            input_string
        )  # returns a string and a float (a command and a confidence)

    def identify_music(self, input: str, engineering: str = ENGENEERING):
        return self.api.generate(f'"{input}" \n\n {engineering}')

    def prompt_enhancement(self, input: str, engineering: str):
        return self.api.generate(f'"{input}" \n\n {engineering}')

    def get_moods(self):
        pass

    def get_genres(self):
        pass

    def search_music(
        self,
        prompt: str | None,
        music: str | None = None,
        artist: str | None = None,
        genres: list[str] = [],
        moods: list[str] = [],
        newer: bool | None = None,
        rec_amount=10,
        doc_amount=1000,
    ):
        if None == music and prompt != None:
            music = self.identify_music(prompt)
        restrictive = genres or moods or music or artist or newer
        return self.api.search_music(
            self.archivist.df,
            rec_amount=rec_amount,
            doc_size=doc_amount,
            has_restriction=restrictive,
            prompt= prompt if prompt else None,
            prefered_genres=genres,
            prefered_moods=moods,
            song_name=music,
            artist=artist,
            most_recent=newer,
        )


@st.cache_resource
def get_back(token, data_path):
    return Back(token, data_path)
