import os
from os import path

from src.character import Character, CharacterItem, CharacterStats
from src.data.store import WorldStore
from src.data.world import World, DefaultClasses, DefaultRaces
from src.ui import create_window


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))

    store = WorldStore()

    save_path = os.path.join(current_dir, "..", "save.dat")
    if path.isfile(save_path):
        store.load(save_path)
        print("Loaded existing worlds.")
    else:
        print("Save file missing.")

    print(store)

    create_window(store)

    store.save(save_path)
    print("Worlds saved.")

