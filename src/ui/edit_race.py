from PySide6.QtUiTools import loadUiType

from src.character import CharacterRace
from src.ui.util import ui_file_path

Base, Form = loadUiType(ui_file_path("edit_race.ui"))


class EditRaceWindow(Base, Form):
    def __init__(self, race: CharacterRace, parent=None):
        super(self.__class__, self).__init__(parent)

        self.race = race

        self.setupUi(self)

        self.name.setText(race.name)

        self.strengthModifier.setValue(race.modifiers.strength)
        self.dexterityModifier.setValue(race.modifiers.dexterity)
        self.constitutionModifier.setValue(race.modifiers.constitution)
        self.intelligenceModifier.setValue(race.modifiers.intelligence)
        self.wisdomModifier.setValue(race.modifiers.wisdom)
        self.charismaModifier.setValue(race.modifiers.charisma)
