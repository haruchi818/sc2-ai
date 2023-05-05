import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from bot import TerranAgent
from sc2.constants import *

agent = TerranAgent()

run_game(maps.get("Abyssal Reef LE"), [
    Bot(Race.Terran, agent),
    Computer(Race.Zerg, Difficulty.Medium)
], realtime=False)