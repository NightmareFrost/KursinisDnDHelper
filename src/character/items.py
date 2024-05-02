from src.character.stats import CharacterStats


class CharacterItem:
    def __init__(self, name: str, modifiers: CharacterStats, extra: str = ""):
        self.name = name
        self.modifiers = modifiers
        self.extra = extra

    def __str__(self):
        value = f"{self.name}. {self.modifiers}"

        if self.extra:
            value += f"; {self.extra}"

        return value

