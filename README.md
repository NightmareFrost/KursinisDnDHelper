# Introduction
The program is a simple GUI application which assists in tracking of a "Dungeons and Dragons" game.
In the program, the user is able to create a character, and then track their progress in the game. \
It is written in Python, and uses the `PySide6` library for the GUI. 

To run the program you need Python 3.11 or later, then you can open the program by using either `Visual Studio Code` or `PyCharm`, by using their inbuilt run operations. 

When you first start the program, you will need to create a new world. Then, you will be asked to create all of your characters, and set their classes and races. When you're done, you can then start the game. While in the game, you can view the status of your characters, and you can also use the inbuilt dice roller to roll the dice.
There's also an edit items button, which allows you to edit the items that are in the game.

# Analysis of the Implementation
There are two character traits: class and race. They are implemented using one common base class: 
```python
class CharacterTrait:
    def __init__(self, name: str, modifiers: CharacterStats):
        self.name = name
        self.modifiers = modifiers
```
A common class used because both classes and races have a name and modifiers. 

To support custom classes and races, all of them are kept track in registries:
```python
class Registry(Generic[_T_co]):
    def __init__(self):
        self.map: dict[str, _T_co] = {}
```
It maps unique identifiers to objects, so that we can store those objects by reference for storing and loading characters. 

Stats are used by items, traits and characters (for base stats). They are implemented as a class:
```python
class CharacterStats:
    def __init__(self, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
```

Saving and loading is implemented by using a world store: 
```python
class WorldStore:
    def __init__(self):
        self.worlds: list[World] = []

    def save(self, path: str):
        file = open(path, "wb")
        pickle.dump(self.worlds, file)
        file.close()

    def load(self, path: str):
        file = open(path, "rb")
        self.worlds = pickle.load(file)
        file.close()
```
It saves the data to a file when the user closes the program, and then loads it back in when the user opens it back in binary form using `pickle`.

The program also has unit tests for the main functions of the program, such as characters and stats. 

# Faced Challenges
* I faced some challenges in dividing the project into smaller, more manageable pieces. I tried to do it in one go, but then I realized that it would be better to do it in smaller steps.
* At first I couldn't figure out how to use unit tests. I thoroughly studied the documentation for `unittest`, and then finally did it.
* It was challenging to make a GUI for my application, because I haven't had any previous experience with `PySide6`.
* At first I tried to reference character traits directly, but then figured out that `pickle` does not recognize when a single instance is used in multiple places. I solved it by introducing registries.

# Conclusions 
I have learned a lot from this project, and I have gained a better understanding of how to use different libraries and projects, and study their documentation. I also learned how it is important to break down the project into small pieces for manageability. Furthermore, my program could be extended by adding more features, such as more types of traits, or by adding more options to items. 

# References
* https://docs.python.org/3.11/
* https://doc.qt.io/qt.html
