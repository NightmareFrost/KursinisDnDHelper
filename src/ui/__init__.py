import os
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCoreApplication, Qt

from src.data.store import WorldStore
from src.ui.main_window import MainWindow


def create_window(store: WorldStore):
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts, True)

    app = QApplication(sys.argv)

    window = MainWindow(store)
    window.show()

    app.exec()
