import sys
import pygame
from setup.settings import Settings
from models.ship import Ship


def run_game():
    pygame.init()

    #screen settings
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #player_ship
    ship = Ship(screen)

    #condition to run
    while True:
        # keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(settings.bg_color)
        ship.blitme()
        # flip == display most recent screen drawn
        pygame.display.flip()

run_game()
