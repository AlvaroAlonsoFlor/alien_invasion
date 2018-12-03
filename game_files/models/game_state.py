import pygame

class GameState():

    def __init__(self, settings):
        self.game_active = False
        self.settings = settings
        self.score = 0
        self.reset_stats()
    
    def reset_stats(self):
        self.score = 0
        self.ships_left = self.settings.ship_limit
        
