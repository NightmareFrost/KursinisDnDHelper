from PySide6.QtUiTools import loadUiType

from src.character import Character, CharacterItem, CharacterStats
from src.ui.edit_item import EditItemWindow
from src.ui.util import ui_file_path

Base, Form = loadUiType(ui_file_path("edit_items.ui"))


class EditItemsWindow(Base, Form):
    def __init__(self, character: Character, parent=None):
        super(self.__class__, self).__init__(parent)

        self.character = character

        self.setupUi(self)

        self.addBtn.clicked.connect(lambda: self.add())
        self.editBtn.clicked.connect(lambda: self.edit())
        self.removeBtn.clicked.connect(lambda: self.remove())

        self.itemsList.currentItemChanged.connect(lambda: self.update_stats())

        self.reinit()

    def reinit(self):
        self.itemsList.clear()

        for item in self.character.items:
            self.itemsList.addItem(item.name)

        self.update_stats()

    def update_stats(self):
        current = self.get_current()

        if current is None:
            self.stats.setText("...")
            return

        newline = "\n"
        self.stats.setText(f"{current.modifiers.join_to_string(newline, True)}\n\n{current.extra}")

    def get_current(self) -> CharacterItem | None:
        row = self.itemsList.currentRow()

        if row == -1:
            return None

        return self.character.items[row]

    def open_window(self, item: CharacterItem):
        window = EditItemWindow(item, self)

        def on_finished(result: int):
            if not result:
                return

            item.name = window.name.text()
            item.extra = window.extra.toPlainText()

            item.modifiers.strength = window.strength.value()
            item.modifiers.dexterity = window.dexterity.value()
            item.modifiers.constitution = window.constitution.value()
            item.modifiers.intelligence = window.intelligence.value()
            item.modifiers.wisdom = window.wisdom.value()
            item.modifiers.charisma = window.charisma.value()

        window.finished.connect(on_finished)

        window.exec_()

    def add(self):
        item = CharacterItem("New Item", CharacterStats())
        self.open_window(item)
        self.character.items.append(item)
        self.reinit()

    def edit(self):
        item = self.get_current()

        if item is None:
            return

        self.open_window(item)
        self.reinit()

    def remove(self):
        item = self.get_current()

        if item is None:
            return

        self.character.items.remove(item)
        self.reinit()

