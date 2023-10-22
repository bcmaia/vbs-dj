from .runner import front_runner

class Front:
    def __init__(self):
        pass

    def setup(self, backref):
        self.__backref = backref
    
    def run(self):
        front_runner(self.__backref)