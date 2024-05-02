from PySide6.QtUiTools import loadUiType

from src.ui.util import ui_file_path

Form, Base = loadUiType(ui_file_path("new_world.ui"))


class NewWorldWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.setupUi(self)

