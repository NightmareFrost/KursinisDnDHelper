import copy
import textwrap

from src.character.items import CharacterItem
from src.character.stats import CharacterStats
from src.character.traits import CharacterRace, CharacterClass
from src.util.registry import Registry


class Character:
    def __init__(self, name: str, clazz: str, race: str):
        self.name = name
        self.clazz = clazz
        self.race = race
        self.base_stats = CharacterStats()
        self.items: list[CharacterItem] = []

    def get_class(self, registry: Registry[CharacterClass]) -> CharacterClass:
        return registry.from_id(self.clazz)

    def get_race(self, registry: Registry[CharacterRace]) -> CharacterRace:
        return registry.from_id(self.race)

    def get_stats(self, class_registry: Registry[CharacterClass], race_registry: Registry[CharacterRace]) -> CharacterStats:
        actual_stats = copy.copy(self.base_stats)

        clazz = self.get_class(class_registry)
        race = self.get_race(race_registry)

        actual_stats.mutate(clazz.modifiers)
        actual_stats.mutate(race.modifiers)

        actual_stats.constraint_min(clazz.constraints_min)
        actual_stats.constraint_max(clazz.constraints_max)

        return actual_stats

    def __str__(self):
        return textwrap.dedent(f"""
            - Character \"{self.name}\":
            - - Class: {self.clazz}
            - - Race: {self.race}
            - - Stats: unknown
            - - Items: {[str(x) for x in self.items]}
        """).strip()

