import cohere
import random
from fuzzywuzzy import fuzz


def get_mood_similarity(row, expected_moods, column_list):

    mood_list = []

    for i in range(8, 30):
        if row[i] == 'High' or row[i] == 'Very High':
            mood_list.append(column_list[i].split('_')[0])
    
    if len(list(set(mood_list))) == 0: return 0
    else: return len(list(set(mood_list) & set(expected_moods))) / len(set(mood_list + expected_moods))

    
def similarity(value, expected_value):
    ratio = fuzz.ratio(value, expected_value)
    if ratio >= 0.7: return ratio
    else: return 0
    

def restriction_search(df, amount=100, song_name=None, artist=None, most_recent=None, prefered_genres=[], prefered_moods=[], weights=[0.33, 0.33, 0.33, 0.33, 0.33]):
    restriction_df = df.copy()
    
    min_year = restriction_df['release_date'].min()
    max_year = restriction_df['release_date'].max()
    if most_recent is None:
        restriction_df['w_year'] = 0
    elif most_recent:
        restriction_df['w_year'] = (restriction_df['release_date']-min_year)/(max_year-min_year)
    else:
        restriction_df['w_year'] = (max_year - restriction_df['release_date'])/(max_year-min_year)

    restriction_df['w_genres'] = 0
    restriction_df.loc[(restriction_df['genre'].isin(prefered_genres)), 'w_genres'] = 1

    #restriction_df['w_song'] = 0
    #restriction_df['w_artist'] = 0

    w_song_list = restriction_df['track_name'].tolist()
    ratio_song_list = [similarity(song, song_name) for song in w_song_list]
    restriction_df['w_song'] = ratio_song_list

    w_artist_list = restriction_df['artist_name'].tolist()
    ratio_artist_list = [similarity(artist_name, artist) for artist_name in w_artist_list]
    restriction_df['w_artist'] = ratio_artist_list

    column_list = df.columns.values.tolist()
    df_list = restriction_df.values.tolist()
    ratio_mood_list = [get_mood_similarity(row, prefered_moods, column_list) for row in df_list]
    restriction_df['w_moods'] = ratio_mood_list

    restriction_df['w'] = (weights[0]*restriction_df['w_song'] + weights[1]*restriction_df['w_artist'] + weights[2]*restriction_df['w_year'] + weights[3]*restriction_df['w_genres'] + weights[4]*restriction_df['w_moods'])/sum(weights)

    return restriction_df.sort_values(by='w', ascending=False).head(amount)



def song_string(df, songId):
    song_dict = df.loc[(df.Id==songId)].to_dict(orient="records")[0]

    final_string = ''
    for key in song_dict:
        if song_dict[key] != 'Average':
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


def string_many_songs(
    df,
    how_many=100,
    has_restriction=False,
    song_name=None,
    artist=None,
    most_recent=None,
    prefered_genres=[],
    prefered_moods=[],
    weights=[0.33, 0.33, 0.33, 0.33, 0.33],
):
    if has_restriction:
        restricted_df = restriction_search(
            df,
            how_many,
            song_name,
            artist,
            most_recent,
            prefered_genres,
            prefered_moods,
            weights,
        )
        sample_ids = random.sample(restricted_df["Id"].unique().tolist(), how_many)
    else:
        sample_ids = random.sample(df["Id"].unique().tolist(), how_many)

    string_list = []
    for song in sample_ids:
        aux_list = []
        aux_list.append(song_string(df, song))
        aux_list.append(song)
        string_list.append(aux_list)

    return string_list


class ApiMaster:
    def __init__(self, token: str, active: bool) -> None:
        self.__token = token
        self.__active = active
        self.__co = None

    def connect(self):
        if not self.__active:
            return self
        self.__co = cohere.Client(self.__token)
        return self

    def embed(self, txt):
        if not self.__active:
            return None
        txt = [str(x) for x in txt] if isinstance(txt, list) else [str(txt)]
        return self.__co.embed(
            texts=txt,
            model="small",
        ).embeddings

    def rerank(self, query, docs, top_n):
        if not self.__active:
            return None
        if not isinstance(docs, list):
            docs = [docs]

        return self.__co.rerank(
            model="rerank-english-v2.0", query=query, documents=docs, top_n=top_n
        ).results

    def generate(self, prompt):
        if not self.__active:
            return None

        return self.__co.generate(prompt=prompt).generations[0].strip()

    def search_music(
        self,
        df,
        rec_amount=3,
        doc_size=1000,
        has_restriction=False,
        prompt=None,
        song_name=None,
        artist=None,
        most_recent=None,
        prefered_genres=[],
        prefered_moods=[],
        weights=[0.33, 0.33, 0.33, 0.33, 0.33],
    ):
        if not has_restriction and prompt is None:
            print(
                "Erro! Ao menos um entre has_restriction e has_promp deve ser verdadeiro"
            )
            return -1

        if prompt is None:
            return restriction_search(
                df,
                rec_amount,
                song_name,
                artist,
                most_recent,
                prefered_genres,
                prefered_moods,
                weights,
            ).to_dict(orient="records")

        else:
            complete_values = string_many_songs(
                df,
                doc_size,
                has_restriction,
                song_name,
                artist,
                most_recent,
                prefered_genres,
                prefered_moods,
                weights,
            )

            docs = [l[0] for l in complete_values]

            response = self.__co.rerank(
                model="rerank-english-v2.0",
                query=prompt,
                documents=docs,
                top_n=rec_amount,
            ).results

            songs_dict = {}
            count = 0
            for result in response:
                index = complete_values[result.index][1]
                aux_dict = df.loc[(df.Id == index)].to_dict(orient="records")[0]
                songs_dict[count] = aux_dict
                count += 1

            return songs_dict
