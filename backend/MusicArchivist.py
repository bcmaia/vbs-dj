import json
import numpy as np
import pandas as pd
import random
import warnings

# Deals with the files
class MusicArchivist:

    def __init__(self, music_file_path : str) -> None:
        songs = pd.read_csv(music_file_path) # Reading
        songs.rename(columns={'Unnamed: 0': 'Id'}, inplace=True) # Renaming

        warnings.filterwarnings("ignore") # Hides the depracation warnings

        # Mapping the ids
        map_songs = {song: idx for idx, song in enumerate(songs.Id.unique())}
        songs['Id'] = songs['Id'].map(map_songs)
        
        self.__musics = self.stardardise_values(songs)

    # Instances the dataframe with music data
    @property
    def df(self):
        return self.__musics

    # Calculate the similarity between the embeddings of two songs
    def calculate_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    # Converts numeric values to natural language representation
    @staticmethod
    def stardardise_values(df):
        valid_columns = df.columns.values.tolist()
        valid_columns = [valid_columns[i] for i in range(7, 29)]

        for column in valid_columns:
            mean = df[column].mean()
            
            std = df[column].std()
            
            new_name = column + '_rating'
            df.loc[(df[column] > mean + 2*std), new_name] = 'Very High'
            df.loc[(df[column] > mean + std) & (df[column] <= mean + 2*std), new_name] = 'High'
            df.loc[(df[column] >= mean - std) & (df[column] <= mean + std), new_name] = 'Average'
            df.loc[(df[column] < mean - std) & (df[column] >= mean - 2*std), new_name] = 'Low'
            df.loc[(df[column] < mean - 2*std), new_name] = 'Very Low'

            df = df.drop(columns=[column])
        df = df.drop(columns=['age'])
        return df

    # Converts music data to natural language formatting
    @staticmethod
    def music_to_str(self, df, songId):
        song_dict = df.loc[(df.Id==songId)].to_dict(orient="records")[0]

        final_string = ''
        for key in song_dict:
            if song_dict[key] != 'Low' and song_dict[key] != 'Very Low' and song_dict[key] != 'Average':
                if key != 'lyrics' and key != 'Id' and key != 'len':
                    names = key.split('_')
                    
                    if len(names) == 2:
                        final_string += "{} {}: {}\n".format(names[0], names[1], song_dict[key])
                    else:
                        final_string += "{}: {}\n".format(names[0], song_dict[key])
                elif key == 'len':
                    final_string += "lyric length: {}\n".format(song_dict[key])

        final_string += "lyrics: \n {}\n\n".format(song_dict['lyrics'])
        return final_string

    # Requests a number of samples from the test data and turns them into natural language
    def get_strings(self, num):
        df = self.__musics.copy()
        sample_ids = random.sample(df['Id'].unique().tolist(), num)
        
        string_list = []
        for song in sample_ids:
            string_list.append(self.music_to_str(self, df, song))

        return string_list