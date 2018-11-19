import sys
import pygame
from setup.settings import Settings
from models.ship import Ship
from helpers.game_functions import *
from models.bullet import Bullet
from pygame.sprite import Group


def run_game():
    pygame.init()

    # screen settings
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # player_ship
    ship = Ship(screen, settings)

    # Bullets
    bullets = Group()

    # Conditions to run
    while True:
        check_events(ship, settings, screen, bullets)
        ship.update_position()
        bullets.update()       
        update_screen(settings, ship, screen, bullets)

run_game()
