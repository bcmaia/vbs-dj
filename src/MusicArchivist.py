import json
import numpy as np
import pandas as pd

class MusicArchivist:
    def __init__(self, music_file_path : str) -> None:
        songs = pd.read_csv(music_file_path) # Reading
        songs.rename(columns={'Unnamed: 0': 'Id'}, inplace=True) # Renaming

        # Mapping the ids
        map_songs = {song: idx for idx, song in enumerate(songs.Id.unique())}
        songs['Id'] = songs['Id'].map(map_songs)
        
        self.musics = songs

    def calculate_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    @staticmethod
    def music_to_str(music):
        s = f"title: "

    def get_strings (self):
        df = self.df.copy()
        songlist = df['Id'].unique().tolist()

        for song in songlist:
            song = df.loc[(df.Id==song)].to_dict()

    def save(self, name):
        


