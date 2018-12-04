import pygame
import os

class GameState():

    def __init__(self, settings):
        self.game_active = False
        self.settings = settings
        self.score = 0
        self.reset_stats()

        # High score
        path = os.path.abspath('score.txt')
        file = open(path, 'r')
        self.high_score = file.read()
        
    
    def reset_stats(self):
        self.score = 0
        self.ships_left = self.settings.ship_limit
        
