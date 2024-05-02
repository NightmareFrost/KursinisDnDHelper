from src.character.stats import CharacterStats


class CharacterTrait:
    def __init__(self, name: str, modifiers: CharacterStats):
        self.name = name
        self.modifiers = modifiers

    def __str__(self):
        return self.name


class CharacterRace(CharacterTrait):
    def __init__(self, name: str, modifiers: CharacterStats):
        super().__init__(name, modifiers)


class CharacterClass(CharacterTrait):
    def __init__(self, name: str, modifiers: CharacterStats, constraints_min: CharacterStats,
                 constraints_max: CharacterStats):
        super().__init__(name, modifiers)

        self.constraints_min = constraints_min
        self.constraints_max = constraints_max
