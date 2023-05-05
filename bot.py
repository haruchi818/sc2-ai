import random
from sc2.bot_ai import BotAI
from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features
from sc2.constants import UnitTypeId
_PLAYER_SELF = features.PlayerRelative.SELF
_NOT_QUEUED = [0]
_SELECT_ALL = [0]


class TerranAgent(BotAI):
    async def on_step(self, iteration):
        # Build Marines
        barracks = self.units(UnitTypeId.BARRACKS)
        for barrack in barracks.idle:
            if self.can_afford(UnitTypeId.MARINE):
                barrack.train(UnitTypeId.MARINE)

        # Attack the enemy
        if self.units(UnitTypeId.MARINE).amount >= 10:
            for marine in self.units(UnitTypeId.MARINE):
                if marine.is_idle:
                    marine.attack(self.enemy_start_locations[0])

        # Send idle workers to mine minerals
        for scv in self.units(UnitTypeId.SCV).idle:
            mineral_field = self.state.mineral_field.closest_to(scv)
            self.do(scv.gather(mineral_field))

        # Expand the base if needed
        if self.units(UnitTypeId.COMMANDCENTER).amount < 2 and self.can_afford(UnitTypeId.COMMANDCENTER):
            await self.expand_now()
    async def build_barracks(self):
        if self.can_afford(UnitTypeId.BARRACKS) and not self.already_pending(UnitTypeId.BARRACKS):
            if self.units(UnitTypeId.SUPPLYDEPOT).ready.exists:
                if self.units(UnitTypeId.BARRACKS).amount < 2:
                    position = self.units(UnitTypeId.SUPPLYDEPOT).random.position
                    await self.build(UnitTypeId.BARRACKS, near=position)
    async def train_marines(self):
        for barracks in self.units(UnitTypeId.BARRACKS).ready.noqueue:
            if self.can_afford(UnitTypeId.MARINE):
                await self.do(barracks.train(UnitTypeId.MARINE))
    def units(self, unit_type):
        return self.observation.player_common.minerals, self.observation.player_common.vespene, self.units(unit_type)




# class TerranAgent(BotAI):
#     def __init__(self):
#         super(TerranAgent, self).__init__()

#         self.attack_coordinates = None

#     def get_units_by_type(self, obs, unit_type):
#         return [unit for unit in obs.observation['feature_units']
#                 if unit.unit_type == unit_type]

#     def step(self, obs):
#         super(TerranAgent, self).step(obs)

#         if obs.first():
#             player_y, player_x = (obs.observation['feature_minimap'][_PLAYER_SELF] == 1).nonzero()
#             xmean = player_x.mean()
#             ymean = player_y.mean()

#             if xmean <= 31 and ymean <= 31:
#                 self.attack_coordinates = (49, 49)
#             else:
#                 self.attack_coordinates = (12, 16)

#         marines = self.get_units_by_type(obs, units.Terran.Marine)

#         if len(marines) >= 15:
#             if self.unit_type_is_selected(obs, units.Terran.Marine):
#                 if self.can_do(obs, actions.FUNCTIONS.Attack_minimap.id):
#                     return actions.FUNCTIONS.Attack_minimap("now", self.attack_coordinates)

#             if self.can_do(obs, actions.FUNCTIONS.select_army.id):
#                 return actions.FUNCTIONS.select_army("select")

#         if len(marines) < 15:
#             for marine in marines:
#                 if marine.x > 25 and self.unit_type_is_selected(obs, units.Terran.Marine):
#                     if self.can_do(obs, actions.FUNCTIONS.Attack_minimap.id):
#                         return actions.FUNCTIONS.Attack_minimap("now", self.attack_coordinates)

#             if self.can_do(obs, actions.FUNCTIONS.select_army.id):
#                 return actions.FUNCTIONS.select_army("select")

#         barracks = self.get_units_by_type(obs, units.Terran.Barracks)
#         if len(barracks) == 0:
#             if self.unit_type_is_selected(obs, units.Terran.SCV):
#                 if self.can_do(obs, actions.FUNCTIONS.Build_Barracks_screen.id):
#                     x = random.randint(0, 83)
#                     y = random.randint(0, 83)
#                     return actions.FUNCTIONS.Build_Barracks_screen("now", (x, y))

#             scvs = self.get_units_by_type(obs, units.Terran.SCV)
#             if len(scvs) > 0:
#                 scv = random.choice(scvs)
#                 return actions.FUNCTIONS.select_point("select", (scv.x, scv.y))

#         else:
#             if self.unit_type_is_selected(obs, units.Terran.Barracks):
#                 if self.can_do(obs, actions.FUNCTIONS.Train_Marine_quick.id):
#                     return actions.FUNCTIONS.Train_Marine_quick("now")

#             barracks = self.get_units_by_type(obs, units.Terran.Barracks)
#             if len(barracks) > 0:
#                 barracks = random.choice(barracks)
#                 return actions.FUNCTIONS.select_point("select", (barracks.x, barracks.y))

#         return actions.FUNCTIONS.no_op()
