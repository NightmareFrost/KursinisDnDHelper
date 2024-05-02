import random

from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent
from PySide6.QtUiTools import loadUiType

from src.ui.util import ui_file_path

Form, Base = loadUiType(ui_file_path("roll_dice.ui"))


class RollDiceWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.setupUi(self)

        self.setWindowFlag(Qt.WindowType.Dialog)
        self.setWindowModality(Qt.WindowModality.WindowModal)

        self.rollBtn.clicked.connect(lambda: self.roll())

        self.choices = [
            (1, 4),
            (1, 6),
            (1, 8),
            (1, 10),
            (1, 12),
            (1, 20)
        ]

    def roll(self):
        row = self.choice.currentIndex()
        min_value, max_value = self.choices[row]

        result = random.randint(min_value, max_value)

        self.result.setText(
            str(result)
        )

    def closeEvent(self, event: QCloseEvent):
        self.parent().show()
