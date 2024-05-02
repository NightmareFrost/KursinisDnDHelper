import pickle

from src.data.world import World


class WorldStore:
    def __init__(self):
        self.worlds: list[World] = []

    def save(self, path: str):
        file = open(path, "wb")
        pickle.dump(self.worlds, file)
        file.close()

    def load(self, path: str):
        file = open(path, "rb")
        self.worlds = pickle.load(file)
        file.close()

    def __str__(self):
        return "\n".join([str(x) for x in self.worlds])
