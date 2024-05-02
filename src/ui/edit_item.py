from PySide6.QtUiTools import loadUiType

from src.character import Character, CharacterItem, CharacterStats
from src.ui.util import ui_file_path

Base, Form = loadUiType(ui_file_path("edit_item.ui"))


class EditItemWindow(Base, Form):
    def __init__(self, item: CharacterItem, parent=None):
        super(self.__class__, self).__init__(parent)

        self.item = item

        self.setupUi(self)

        self.name.setText(item.name)
        self.extra.setPlainText(item.extra)

        self.strength.setValue(item.modifiers.strength)
        self.dexterity.setValue(item.modifiers.dexterity)
        self.constitution.setValue(item.modifiers.constitution)
        self.intelligence.setValue(item.modifiers.intelligence)
        self.wisdom.setValue(item.modifiers.wisdom)
        self.charisma.setValue(item.modifiers.charisma)
