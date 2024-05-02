from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent
from PySide6.QtUiTools import loadUiType

from src.character import Character
from src.data.world import World
from src.ui.edit_items import EditItemsWindow
from src.ui.roll_dice import RollDiceWindow
from src.ui.util import ui_file_path

Form, Base = loadUiType(ui_file_path("game.ui"))


class GameWindow(Base, Form):
    def __init__(self, world: World, parent=None):
        super(self.__class__, self).__init__(parent)

        self.world = world

        self.setupUi(self)

        self.setWindowFlag(Qt.WindowType.Window)

        self.worldName.setText(world.name)

        self.rollDice.clicked.connect(lambda: self.roll_dice())
        self.editItems.clicked.connect(lambda: self.edit_items())

        self.characters.clear()

        for character in world.characters:
            self.characters.addItem(character.name)

        self.characters.currentItemChanged.connect(lambda: self.update_stats())

        self.update_stats()

    def get_current(self) -> Character | None:
        row = self.characters.currentRow()

        if row == -1:
            return None

        return self.world.characters[row]

    def update_stats(self):
        character = self.get_current()

        if character is None:
            self.stats.setText("...")
            return

        stats = character.get_stats(self.world.classes, self.world.races)
        self.stats.setText(stats.join_to_string("\n", False))

    def roll_dice(self):
        window = RollDiceWindow(self)
        window.show()

    def edit_items(self):
        character = self.get_current()

        if character is None:
            return

        window = EditItemsWindow(character, self)
        window.exec_()

    def closeEvent(self, event: QCloseEvent):
        self.parent().show()
