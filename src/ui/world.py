from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QListWidgetItem

from src.character import Character
from src.data.world import World, DefaultClasses, DefaultRaces
from src.ui.custom_content import CustomContentWindow
from src.ui.edit_character import EditCharacterWindow
from src.ui.game import GameWindow
from src.ui.util import ui_file_path

Form, Base = loadUiType(ui_file_path("world.ui"))


class WorldWindow(Base, Form):
    def __init__(self, world: World, parent=None):
        super(self.__class__, self).__init__(parent)

        self.world = world

        self.setupUi(self)

        self.setWindowFlag(Qt.WindowType.Window)

        self.startBtn.clicked.connect(lambda: self.start())
        self.newBtn.clicked.connect(lambda: self.new())
        self.editBtn.clicked.connect(lambda: self.edit())
        self.deleteBtn.clicked.connect(lambda: self.delete())
        self.customContent.clicked.connect(lambda: self.custom_content())

        self.list.itemDoubleClicked.connect(lambda: self.edit())

        self.items: list[(QListWidgetItem, Character)] = []

        self.reinit()

    def reinit(self):
        self.worldName.setText(self.world.name)

        self.items.clear()
        self.list.clear()

        for character in self.world.characters:
            item = QListWidgetItem(character.name)

            self.list.addItem(item)
            self.items.append((item, character))

    def get_current(self) -> Character | None:
        for key, value in self.items:
            if key == self.list.currentItem():
                return value

        return None

    def start(self):
        window = GameWindow(self.world, self)
        window.show()
        self.hide()

    def edit_character(self, character: Character) -> bool:
        window = EditCharacterWindow(self.world, character, self)

        def on_accepted():
            character.name = window.name.text()
            character.clazz = self.world.classes.get_id(window.class_options[window.clazz.currentIndex()])
            character.race = self.world.races.get_id(window.race_options[window.race.currentIndex()])

        window.accepted.connect(lambda: on_accepted())

        window.exec_()

        return True

    def new(self):
        clazz = list(self.world.classes.map.keys())[0]
        race = list(self.world.races.map.keys())[0]

        character = Character("New Character", clazz, race)

        if self.edit_character(character):
            character.base_stats.randomize()

            self.world.characters.append(character)

            self.reinit()

    def edit(self):
        character = self.get_current()

        if character is None:
            return

        self.edit_character(character)
        self.reinit()

    def delete(self):
        character = self.get_current()

        if character is None:
            return

        self.world.characters.remove(character)
        self.reinit()

    def custom_content(self):
        window = CustomContentWindow(self.world, self)
        window.exec_()

    def closeEvent(self, event: QCloseEvent):
        self.parent().show()
