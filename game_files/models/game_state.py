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
        file.close()
        
    
    def reset_stats(self):
        self.score = 0
        self.ships_left = self.settings.ship_limit
    
    def update_high_score(self, new_score):

        if self.high_score == '':
            self.high_score = 0

        if int(self.high_score) < int(new_score):
            path = os.path.abspath('score.txt')
            file = open(path, 'w')
            file.write(str(new_score))
            file.close()

        
