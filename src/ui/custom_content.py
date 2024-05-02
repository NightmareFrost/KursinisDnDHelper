import random

from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QMessageBox

from src.character import CharacterClass, CharacterRace, CharacterStats
from src.data.world import World
from src.ui.edit_class import EditClassWindow
from src.ui.edit_race import EditRaceWindow
from src.ui.util import ui_file_path

Base, Form = loadUiType(ui_file_path("custom_content.ui"))


class CustomContentWindow(Base, Form):
    def __init__(self, world: World, parent=None):
        super(self.__class__, self).__init__(parent)

        self.world = world

        self.setupUi(self)

        self.class_options: list[CharacterClass] = list(world.classes.map.values())
        self.race_options: list[CharacterRace] = list(world.races.map.values())

        self.reinit()

        self.newClass.clicked.connect(lambda: self.new_class())
        self.editClass.clicked.connect(lambda: self.edit_class())
        self.removeClass.clicked.connect(lambda: self.remove_class())

        self.newRace.clicked.connect(lambda: self.new_race())
        self.editRace.clicked.connect(lambda: self.edit_race())
        self.removeRace.clicked.connect(lambda: self.remove_race())

        self.classes.itemDoubleClicked.connect(lambda: self.edit_class())
        self.races.itemDoubleClicked.connect(lambda: self.edit_race())

    def get_current_class(self) -> CharacterClass | None:
        index = self.classes.currentRow()

        if index == -1:
            return None

        return self.class_options[index]

    def get_current_race(self) -> CharacterRace | None:
        index = self.races.currentRow()

        if index == -1:
            return None

        return self.race_options[index]

    def open_class_window(self, clazz: CharacterClass):
        window = EditClassWindow(clazz, self)

        def on_finished(result: int):
            if not result:
                return

            clazz.name = window.name.text()

            clazz.modifiers.strength = window.strengthModifier.value()
            clazz.modifiers.dexterity = window.dexterityModifier.value()
            clazz.modifiers.constitution = window.constitutionModifier.value()
            clazz.modifiers.intelligence = window.intelligenceModifier.value()
            clazz.modifiers.wisdom = window.wisdomModifier.value()
            clazz.modifiers.charisma = window.charismaModifier.value()

            clazz.constraints_min.strength = window.strengthMin.value()
            clazz.constraints_min.dexterity = window.dexterityMin.value()
            clazz.constraints_min.constitution = window.constitutionMin.value()
            clazz.constraints_min.intelligence = window.intelligenceMin.value()
            clazz.constraints_min.wisdom = window.wisdomMin.value()
            clazz.constraints_min.charisma = window.charismaMin.value()

            clazz.constraints_max.strength = window.strengthMax.value()
            clazz.constraints_max.dexterity = window.dexterityMax.value()
            clazz.constraints_max.constitution = window.constitutionMax.value()
            clazz.constraints_max.intelligence = window.intelligenceMax.value()
            clazz.constraints_max.wisdom = window.wisdomMax.value()
            clazz.constraints_max.charisma = window.charismaMax.value()

        window.finished.connect(on_finished)

        window.exec_()

    def open_race_window(self, race: CharacterRace):
        window = EditRaceWindow(race, self)

        def on_finished(result: int):
            if not result:
                return

            race.name = window.name.text()

            race.modifiers.strength = window.strengthModifier.value()
            race.modifiers.dexterity = window.dexterityModifier.value()
            race.modifiers.constitution = window.constitutionModifier.value()
            race.modifiers.intelligence = window.intelligenceModifier.value()
            race.modifiers.wisdom = window.wisdomModifier.value()
            race.modifiers.charisma = window.charismaModifier.value()

        window.finished.connect(on_finished)

        window.exec_()

    def new_class(self):
        clazz = CharacterClass("New Class", CharacterStats(), CharacterStats.new_min(), CharacterStats.new_max())
        self.open_class_window(clazz)
        self.world.classes.register(f"custom_{random.randint(0, 999999)}", clazz)
        self.reinit()

    def edit_class(self):
        clazz = self.get_current_class()

        if clazz is None:
            return

        self.open_class_window(clazz)
        self.reinit()

    def remove_class(self):
        clazz = self.get_current_class()

        if clazz is None:
            return

        if len(self.world.classes.map) <= 1:
            QMessageBox.critical(self, "Failed", "At least one class is required.")
            return

        class_id = self.world.classes.get_id(clazz)
        self.world.classes.unregister(class_id)

        self.world.reassign_classes(class_id)

        self.reinit()

    def new_race(self):
        race = CharacterRace("New Race", CharacterStats())
        self.open_race_window(race)
        self.world.races.register(f"custom_{random.randint(0, 999999)}", race)
        self.reinit()

    def edit_race(self):
        race = self.get_current_race()

        if race is None:
            return

        self.open_race_window(race)
        self.reinit()

    def remove_race(self):
        race = self.get_current_race()

        if race is None:
            return

        if len(self.world.races.map) <= 1:
            QMessageBox.critical(self, "Failed", "At least one race is required.")
            return

        race_id = self.world.races.get_id(race)
        self.world.races.unregister(race_id)

        self.world.reassign_races(race_id)

        self.reinit()

    def reinit(self):
        self.class_options = list(self.world.classes.map.values())
        self.race_options = list(self.world.races.map.values())

        self.classes.clear()
        self.races.clear()

        for clazz in self.class_options:
            self.classes.addItem(clazz.name)

        for race in self.race_options:
            self.races.addItem(race.name)
