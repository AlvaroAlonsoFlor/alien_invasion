import sys
import pygame
from setup.settings import Settings


def run_game():
    pygame.init()

    settings = Settings()
    #screen settings
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #condition to run
    while True:
        # keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(settings.bg_color)
        # flip == display most recent screen drawn
        pygame.display.flip()

run_game()
