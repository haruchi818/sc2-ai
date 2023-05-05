import unittest
from bot import TerranAgent
from sc2.constants import UnitTypeId
class TestTerranAgent(unittest.TestCase):
    def setUp(self):
        self.agent = TerranAgent()

    def test_build_barracks(self):
        self.agent.build_barracks()
        self.assertTrue(self.agent.units("Barracks").exists)

    def test_train_marines(self):
        self.agent.on_step(0)
        self.assertGreaterEqual(self.agent.units(UnitTypeId.MARINE).amount, 1)


if __name__ == "__main__":
    unittest.main()