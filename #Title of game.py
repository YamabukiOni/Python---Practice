#Title of game
game_title: GardenSpace

#Description
"""A garden game :P"""

import random

class = Plant
def __init__(self, name, harvest_yield):
    self.name = name
    self.harvest_yield = harvest_yield
    self.growth_stages = ["seed", "sprout", "mature", "flower", "fruit"]
    self.current_growth_stage = self.growth_stage[0] #initial growth stage is seed
    harvestable = False

def grow(self):
    current_index = self.growth_stages.index(self.current_growth_stage)
    