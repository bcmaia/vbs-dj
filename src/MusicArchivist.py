import json
import numpy as np
import pandas as pd

class MusicArchivist:
    musics = None

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
    def music_to_str(self, songId):
        song_dict = self.musics.loc[(self.musics.Id==songId)].to_dict(orient="records")[0]
        print(songId)

        final_string = ''
        for key in song_dict:
            if key != 'lyrics' and key != 'Id':
                final_string += "{}: {}\n".format(key, song_dict[key])

        final_string += "lyrics: \n {}\n\n".format(song_dict['lyrics'])
        return final_string

    def get_strings(self, num):
        df = self.musics.copy()
        songlist = df['Id'].unique().tolist()
        songlist = songlist[0:num]

        strings = []
        for song in songlist:
            strings.append(self.music_to_str(self, song))

        return strings

    # def save(self, name):
    #     print(self.get_strings())
        