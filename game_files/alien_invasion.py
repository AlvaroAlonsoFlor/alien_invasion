import sys
import pygame
from setup.settings import Settings
from models.ship import Ship
from helpers.game_functions import *


def run_game():
    pygame.init()

    #screen settings
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #player_ship
    ship = Ship(screen)

    #conditions to run
    while True:
        check_events()       
        update_screen(settings, ship, screen)

run_game()
