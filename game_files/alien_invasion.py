import sys
import os
import pygame
from setup.settings import Settings
from models.ship import Ship
from helpers.game_functions import *
from models.bullet import Bullet
from pygame.sprite import Group
from models.alien import Alien
from models.game_state import GameState
from models.button import Button
from models.scoreboard import Scoreboard


def run_game():
    pygame.init()

    # Screen Settings
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Background image
    path = os.path.abspath('game_files/images/space_background.png')
    background_img = pygame.image.load(path)

    # Game State
    game_state = GameState(settings)

    # Scoreboard
    scoreboard = Scoreboard(settings, screen, game_state)

    # Player Ship
    ship = Ship(screen, settings)

    # Bullets
    bullets = Group()

    # Aliens

    aliens = Group()
    create_fleet(settings, screen, aliens, ship)

    # Play

    play_button = Button(settings, screen, "Play")

    # Conditions to run
    
    while True:
        check_events(ship, settings, screen, bullets, play_button, game_state, aliens, scoreboard)

        if game_state.game_active:
                ship.update_position()
                update_bullets(bullets, aliens, game_state, settings, scoreboard)  
                update_aliens(settings, aliens, ship, game_state, screen, bullets, scoreboard)
        update_screen(settings, ship, screen, bullets, aliens, game_state, play_button, scoreboard, background_img)

        

run_game()
