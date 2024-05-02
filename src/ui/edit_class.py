from PySide6.QtUiTools import loadUiType

from src.character import CharacterRace, CharacterClass
from src.ui.util import ui_file_path

Base, Form = loadUiType(ui_file_path("edit_class.ui"))


class EditClassWindow(Base, Form):
    def __init__(self, race: CharacterClass, parent=None):
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

        self.strengthMin.setValue(race.constraints_min.strength)
        self.dexterityMin.setValue(race.constraints_min.dexterity)
        self.constitutionMin.setValue(race.constraints_min.constitution)
        self.intelligenceMin.setValue(race.constraints_min.intelligence)
        self.wisdomMin.setValue(race.constraints_min.wisdom)
        self.charismaMin.setValue(race.constraints_min.charisma)

        self.strengthMax.setValue(race.constraints_max.strength)
        self.dexterityMax.setValue(race.constraints_max.dexterity)
        self.constitutionMax.setValue(race.constraints_max.constitution)
        self.intelligenceMax.setValue(race.constraints_max.intelligence)
        self.wisdomMax.setValue(race.constraints_max.wisdom)
        self.charismaMax.setValue(race.constraints_max.charisma)
