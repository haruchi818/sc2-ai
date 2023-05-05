## PySC2 Bot

This is a PySC2 bot that uses the `sc2` library to play StarCraft II. The bot is written in Python and uses the `TerranAgent` class to control a Terran race army.

### Requirements

- Python 3.6 or higher
- PySC2 3.0 or higher
- StarCraft II game client (version 4.10 or higher)

### Installation

1. Install Python 3.6 or higher on your computer.
2. Install the PySC2 library by running `pip install pysc2` in your terminal.
3. Download and install the StarCraft II game client from the [official website](https://starcraft2.com/en-us/).
4. Set the `SC2PATH` environment variable to point to the StarCraft II game directory. For example, on Windows, you might run `set SC2PATH=C:\Program Files (x86)\StarCraft II` in your terminal.

### Usage

1. Clone the repository to your computer.
2. Open a terminal and navigate to the repository directory.
3. Run the command `python main.py` to start the PySC2 game.
4. Watch the game window to observe your bot's actions and decisions.

### Testing

To run the unit tests for this bot, you can use the `unittest` module included with Python.

Here's an example test file (`test_bot.py`) that tests the behavior of the `TerranAgent` class:

```python
import unittest
from bot import TerranAgent

class TestTerranAgent(unittest.TestCase):
    def setUp(self):
        self.agent = TerranAgent()

    def test_build_barracks(self):
        self.agent.build_barracks()
        self.assertTrue(self.agent.units("Barracks").exists)

    def test_train_marines(self):
        self.agent.build_barracks()
        self.agent.train_marines()
        self.assertGreaterEqual(self.agent.units("Marine").amount, 1)

if __name__ == "__main__":
    unittest.main()
```

This test file defines two test methods (`test_build_barracks` and `test_train_marines`) that test the behavior of the `build_barracks` and `train_marines` methods of the `TerranAgent` class.

To run the tests, you can use the command `python test_bot.py` in your terminal. If all of the tests pass, you should see a message indicating that the tests were successful. If any of the tests fail, you will see an error message indicating which test(s) failed and why.

I hope this helps you get started with testing your PySC2 bot! Let me know if you have any questions or need further assistance.
