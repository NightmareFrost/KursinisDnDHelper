import random


class CharacterConstraints:
    max = 100
    min = -max


class CharacterStats:
    @staticmethod
    def new_min(strength=CharacterConstraints.min,
                dexterity=CharacterConstraints.min,
                constitution=CharacterConstraints.min,
                intelligence=CharacterConstraints.min,
                wisdom=CharacterConstraints.min,
                charisma=CharacterConstraints.min) -> "CharacterStats":
        return CharacterStats(strength, dexterity, constitution, intelligence, wisdom, charisma)

    @staticmethod
    def new_max(strength=CharacterConstraints.max,
                dexterity=CharacterConstraints.max,
                constitution=CharacterConstraints.max,
                intelligence=CharacterConstraints.max,
                wisdom=CharacterConstraints.max,
                charisma=CharacterConstraints.max) -> "CharacterStats":
        return CharacterStats(strength, dexterity, constitution, intelligence, wisdom, charisma)

    def __init__(self, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def randomize(self):
        self.strength = random.randint(1, 10)
        self.dexterity = random.randint(1, 10)
        self.constitution = random.randint(1, 10)
        self.intelligence = random.randint(1, 10)
        self.wisdom = random.randint(1, 10)
        self.charisma = random.randint(1, 10)

    def mutate(self, other: "CharacterStats"):
        self.strength += other.strength
        self.dexterity += other.dexterity
        self.constitution += other.constitution
        self.intelligence += other.intelligence
        self.wisdom += other.wisdom
        self.charisma += other.charisma

    def constraint_min(self, other: "CharacterStats"):
        self.strength = max(self.strength, other.strength)
        self.dexterity = max(self.dexterity, other.dexterity)
        self.constitution = max(self.constitution, other.constitution)
        self.intelligence = max(self.intelligence, other.intelligence)
        self.wisdom = max(self.wisdom, other.wisdom)
        self.charisma = max(self.charisma, other.charisma)

    def constraint_max(self, other: "CharacterStats"):
        self.strength = min(self.strength, other.strength)
        self.dexterity = min(self.dexterity, other.dexterity)
        self.constitution = min(self.constitution, other.constitution)
        self.intelligence = min(self.intelligence, other.intelligence)
        self.wisdom = min(self.wisdom, other.wisdom)
        self.charisma = min(self.charisma, other.charisma)

    def join_to_string(self, separator: str, with_format: bool):
        stats = {
            "Strength": self.strength,
            "Dexterity": self.dexterity,
            "Constitution": self.constitution,
            "Intelligence": self.intelligence,
            "Wisdom": self.wisdom,
            "Charisma": self.charisma,
        }

        def format_modifier(value: int):
            if with_format and value > 0:
                return f"+{value}"
            else:
                return str(value)

        return separator.join(
            [f"{k}: {format_modifier(v)}" for k, v in stats.items() if v != 0]
        )

    def __str__(self):
        return self.join_to_string("; ", True)
