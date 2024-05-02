import unittest

from character import CharacterStats, Character
from data.world import DefaultClasses, DefaultRaces, World
from util.registry import Registry


class CharacterStatsTest(unittest.TestCase):
    def test_mutate(self):
        original = CharacterStats(strength=5)
        other = CharacterStats(strength=10, dexterity=5)

        original.mutate(other)

        self.assertEqual(15, original.strength)
        self.assertEqual(5, original.dexterity)

    def test_constraint_max(self):
        original = CharacterStats(intelligence=15)
        other = CharacterStats(intelligence=10)

        original.constraint_max(other)

        self.assertEqual(10, original.intelligence)

    def test_constraint_min(self):
        original = CharacterStats(strength=15)
        other = CharacterStats(strength=30)

        original.constraint_min(other)

        self.assertEqual(30, original.strength)

    def test_join_to_string(self):
        stats = CharacterStats(strength=10, dexterity=-15)

        self.assertEqual("Strength: 10\nDexterity: -15", stats.join_to_string("\n", False))
        self.assertEqual("Strength: +10\nDexterity: -15", stats.join_to_string("\n", True))
        self.assertEqual("Strength: +10; Dexterity: -15", stats.join_to_string("; ", True))


class CharacterTest(unittest.TestCase):
    def __init__(self, method_name: str = "runTest"):
        super().__init__(method_name)

        self.character = Character("Character", DefaultClasses.rogue, DefaultRaces.dwarf)

        self.world = World("Test World")
        self.world.register_defaults()

    def test_props(self):
        self.assertEqual("Character", self.character.name)
        self.assertEqual(DefaultClasses.rogue, self.character.clazz)
        self.assertEqual(DefaultRaces.dwarf, self.character.race)

    def test_stats(self):
        stats = self.character.get_stats(self.world.classes, self.world.races)

        self.assertEqual(1, stats.strength)
        self.assertEqual(0, stats.charisma)


class RegistryTest(unittest.TestCase):
    def test_register(self):
        registry: Registry[str] = Registry()

        registry.register("test", "Test")
        registry.register("test2", "Test2")

        self.assertEqual("Test", registry.from_id("test"))
        self.assertEqual("test", registry.get_id("Test"))

        self.assertEqual("Test2", registry.from_id("test2"))
        self.assertEqual("test2", registry.get_id("Test2"))

    def test_unregister(self):
        registry: Registry[str] = Registry()

        registry.register("test", "Test")

        self.assertIsNotNone(registry.from_id("test"))

        registry.unregister("test")

        self.assertIsNone(registry.from_id("test"))


if __name__ == "__main__":
    unittest.main()
