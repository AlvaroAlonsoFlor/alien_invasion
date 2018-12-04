import pygame.font
from models.ship import Ship
from pygame.sprite import Group

class Scoreboard():

    def __init__(self, settings, screen, game_state):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.game_state = game_state

        # Text
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Initial score
        self.prep_score()

        # Number of ships
        self.prep_ships()

    def prep_score(self):
        score_str = str(self.game_state.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Score display location
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.ships.draw(self.screen)
    
    def prep_ships(self):
        self.ships = Group()

        for ship_number in range(self.game_state.ships_left):
            ship = Ship(self.screen, self.settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
