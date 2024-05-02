from src.character import CharacterClass, CharacterRace, Character, CharacterStats
from src.util.registry import Registry


class DefaultClasses:
    warrior = "warrior"
    rogue = "rogue"
    wizard = "wizard"
    bard = "bard"
    healer = "healer"
    archer = "archer"


class DefaultRaces:
    human = "human"
    elf = "elf"
    dwarf = "dwarf"


class World:
    def __init__(self, name: str):
        self.name = name
        self.characters: list[Character] = []
        self.classes: Registry[CharacterClass] = Registry()
        self.races: Registry[CharacterRace] = Registry()

    def __str__(self):
        newline = "\n\n"
        return f"World \"{self.name}\":\n{newline.join([str(x) for x in self.characters])}"

    def register_defaults(self):
        # Classes
        self.classes.register(DefaultClasses.warrior, CharacterClass("Warrior",
                                 modifiers=CharacterStats(strength=2, constitution=1, intelligence=-1),
                                 constraints_min=CharacterStats.new_min(strength=10),
                                 constraints_max=CharacterStats.new_max(intelligence=10, wisdom=10)))

        self.classes.register(DefaultClasses.rogue, CharacterClass("Rogue",
                               modifiers=CharacterStats(dexterity=2, charisma=1, wisdom=-1),
                               constraints_min=CharacterStats.new_min(dexterity=10),
                               constraints_max=CharacterStats.new_max(wisdom=10)))

        self.classes.register(DefaultClasses.wizard, CharacterClass("Wizard",
                                modifiers=CharacterStats(intelligence=2, wisdom=1, strength=-1),
                                constraints_min=CharacterStats.new_min(intelligence=10, wisdom=5),
                                constraints_max=CharacterStats.new_max(strength=10)))

        self.classes.register(DefaultClasses.bard, CharacterClass("Bard",
                              modifiers=CharacterStats(charisma=2, dexterity=1, strength=-1),
                              constraints_min=CharacterStats.new_min(charisma=10),
                              constraints_max=CharacterStats.new_max(strength=10)))

        self.classes.register(DefaultClasses.healer, CharacterClass("Healer",
                                modifiers=CharacterStats(wisdom=2, charisma=1, dexterity=-1),
                                constraints_min=CharacterStats.new_min(wisdom=10),
                                constraints_max=CharacterStats.new_max(dexterity=10)))

        self.classes.register(DefaultClasses.archer, CharacterClass("Archer",
                                modifiers=CharacterStats(dexterity=2, strength=1, constitution=-1),
                                constraints_min=CharacterStats.new_min(dexterity=10, strength=5),
                                constraints_max=CharacterStats.new_max(constitution=10)))

        # Races
        self.races.register(DefaultRaces.human, CharacterRace("Human", CharacterStats()))
        self.races.register(DefaultRaces.elf, CharacterRace("Elf", CharacterStats(dexterity=1, wisdom=1, strength=-1)))
        self.races.register(DefaultRaces.dwarf, CharacterRace("Dwarf", CharacterStats(strength=1, constitution=1, charisma=-1)))

    def reassign_classes(self, class_id: str):
        for character in self.characters:
            if character.clazz != class_id:
                continue

            character.clazz = list(self.classes.map.keys())[0]

    def reassign_races(self, race_id: str):
        for character in self.characters:
            if character.race != race_id:
                continue

            character.race = list(self.races.map.keys())[0]

