from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QListWidgetItem

from src.character import Character, CharacterClass, CharacterRace
from src.data.world import World, DefaultClasses, DefaultRaces
from src.ui.util import ui_file_path

Form, Base = loadUiType(ui_file_path("edit_character.ui"))


class EditCharacterWindow(Base, Form):
    def __init__(self, world: World, character: Character, parent=None):
        super(self.__class__, self).__init__(parent)

        self.character = character

        self.setupUi(self)

        self.setWindowFlag(Qt.WindowType.Window)

        self.name.setText(self.character.name)

        self.class_options: list[CharacterClass] = list(world.classes.map.values())
        self.race_options: list[CharacterRace] = list(world.races.map.values())

        self.clazz.clear()
        self.race.clear()

        for clazz in self.class_options:
            self.clazz.addItem(clazz.name)

        for race in self.race_options:
            self.race.addItem(race.name)

        self.clazz.setCurrentIndex(self.class_options.index(character.get_class(world.classes)))
        self.race.setCurrentIndex(self.race_options.index(character.get_race(world.races)))

        self.clazz.currentIndexChanged.connect(lambda: self.update_stats())
        self.race.currentIndexChanged.connect(lambda: self.update_stats())

        self.update_stats()

    def update_stats(self):
        self.classStats.setText(
            self.class_options[self.clazz.currentIndex()].modifiers.join_to_string("\n", True)
        )

        self.raceStats.setText(
            self.race_options[self.race.currentIndex()].modifiers.join_to_string("\n", True)
        )


