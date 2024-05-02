import os

from PySide6.QtCore import Qt
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QListWidgetItem

from src.data.store import WorldStore
from src.data.world import World
from src.ui.new_world import NewWorldWindow
from src.ui.util import ui_file_path
from src.ui.world import WorldWindow

Form, Base = loadUiType(ui_file_path("main_window.ui"))


class MainWindow(Base, Form):
    def __init__(self, store: WorldStore, parent=None):
        super(self.__class__, self).__init__(parent)

        self.store = store

        self.setupUi(self)

        self.openBtn.clicked.connect(lambda: self.open_world())
        self.newBtn.clicked.connect(lambda: self.new_world())
        self.deleteBtn.clicked.connect(lambda: self.delete_world())

        self.worldList.itemDoubleClicked.connect(lambda: self.open_world())

        self.items: list[(QListWidgetItem, World)] = []

        self.reinit()

    def open_world_window(self, world: World):
        window = WorldWindow(world, self)
        window.show()
        self.hide()

    def reinit(self):
        self.items.clear()
        self.worldList.clear()

        for world in self.store.worlds:
            item = QListWidgetItem(world.name)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.items.append((item, world))
            self.worldList.addItem(item)

    def open_world(self):
        for key, value in self.items:
            if key != self.worldList.currentItem():
                continue

            self.open_world_window(value)

            break

    def delete_world(self):
        for key, value in self.items:
            if key != self.worldList.currentItem():
                continue

            self.store.worlds.remove(value)
            self.reinit()

            break

    def new_world(self):
        dialog = NewWorldWindow(self)

        def on_finished(result):
            if not result:
                return

            world = World(name=dialog.worldName.text())
            world.register_defaults()
            self.store.worlds.append(world)
            self.reinit()

            self.open_world_window(world)

        dialog.finished.connect(on_finished)

        dialog.exec_()
