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
    
    def save_high_score(self, session_high_score):

        # Get high score from previous games
        path = os.path.abspath('score.txt')
        file = open(path, 'r')
        old_high_score = file.read()
        file.close()

        if old_high_score == '':
            old_high_score = 0

        # Override high score
        if int(old_high_score) < int(session_high_score):
            path = os.path.abspath('score.txt')
            file = open(path, 'w')
            file.write(str(session_high_score))
            file.close()

        
