import json

class MusicArchivist:
    def __init__(self, music_file_path : str) -> None:
        self.__path = music_file_path

        with open(self.__path, 'r') as f:
            self.__musics = json.load(f)

    @property
    def musics(self):
        return self.__musics
    


