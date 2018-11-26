import sys
import pygame
from setup.settings import Settings
from models.ship import Ship
from helpers.game_functions import *
from models.bullet import Bullet
from pygame.sprite import Group
from models.alien import Alien


def run_game():
    pygame.init()

    # Screen Settings
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Player Ship
    ship = Ship(screen, settings)

    # Bullets
    bullets = Group()

    # Aliens

    aliens = Group()
    create_fleet(settings, screen, aliens, ship)

    # Conditions to run
    while True:
        check_events(ship, settings, screen, bullets)
        ship.update_position()
        update_bullets(bullets)  
        update_aliens(aliens)
        update_screen(settings, ship, screen, bullets, aliens)

run_game()