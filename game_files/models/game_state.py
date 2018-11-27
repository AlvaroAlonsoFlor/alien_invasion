import pygame

class GameState():

    def __init__(self, settings):
        self.settings = settings
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit