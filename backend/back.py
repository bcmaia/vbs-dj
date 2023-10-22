from .ApiMaster import ApiMaster
from .MusicArchivist import MusicArchivist
from .classify import classify as classify
import pandas as pd
import streamlit as st
import numpy as np
import json

ENGENEERING = "Answer only with the name of the music as the following example: 'Fur Elise'\nTell me only the name of the music are you being asked to play."

class Back:
    def __init__(self, token: str, data_path):
        self.api = ApiMaster(token, True).connect()
        self.archivist = MusicArchivist(data_path)
        self.embeds_df = pd.read_csv('./data/database_10000.csv')

    def classify_instruction(self, input_string):  # receives a string
        return classify(
            input_string
        )  # returns a string and a float (a command and a confidence)

    def identify_music(self, input: str, engineering: str = ENGENEERING):
        return self.api.generate(f'"{input}" \n\n {engineering}')

    def prompt_enhancement(self, input: str, engineering: str):
        return self.api.generate(f'"{input}" \n\n {engineering}')

    def get_moods(self):
        column_list = self.archivist.df.columns.values.tolist()
        return [column_list[i].split('_')[0] for i in range(8, 30)]

    def get_genres(self):
        return self.archivist.df['genre'].unique()

    def search_music(
        self,
        prompt: str | None,
        music: str | None = None,
        artist: str | None = None,
        genres: list[str] = [],
        moods: list[str] = [],
        newer: bool | None = None,
        rec_amount=10,
        doc_amount=1_000,
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
    
    def calculate_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def entropy_search(self, input: str, top_n=3):
        input_embedding = self.api.embed(input)
        songs = self.embeds_df.copy()
        songs.rename(columns={'Unnamed: 0': 'Id'}, inplace=True)
        map_songs = {song: idx for idx, song in enumerate(songs.Id.unique())}
        songs['Id'] = songs['Id'].map(map_songs)

        embeds = [json.loads(x) for x in songs['embeds']]

        diff = []   
        for embed in embeds:
            diff.append(self.calculate_similarity(input_embedding, embed))
        
        songs['similarity'] = diff
        return songs.sort_values(by='similarity', ascending=False).head(top_n)

    def predict_vibe(self, input, k_means = 10):
        input_embedding = self.api.embed(input)

        df = self.embeds_df.copy()
        similars = self.entropy_search(df, input_embedding, k_means).tolist()
        aux = []
        for i in range(k_means):
            aux.append([similars[i][j] for j in range(7, 29)])

        res = []
        for j in range(0, len(aux[0])):
            tmp = 0
            for i in range(0, len(aux)):
                tmp = tmp + aux[i][j]
            res.append(tmp/k_means)

        prediction={}

        valid_columns = df.columns.values.tolist()
        valid_columns = [valid_columns[i] for i in range(7, 29)]

        index = 0
        for column in valid_columns:

            mean = df[column].mean()
            std = df[column].std()

            if res[index] > mean + 2*std: value="Very High"
            elif res[index ]> mean + std & res[index] <= mean + 2*std: value="High"
            elif res[index] >= mean - std & res[index] <= mean + std: value="Average"
            elif res[index] < mean - std & res[index] >= mean - 2*std: value="Low"
            else: value="Very Low"

            if value=="High" or value=="Very High":
                prediction[column] = value
            index += 1

        return prediction

    def find_next_music(self, df, curr_list):
        pass
        
@st.cache_resource
def get_back(token, data_path):
    return Back(token, data_path)