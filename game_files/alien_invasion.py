import sys
import pygame

def run_game():
    pygame.init()
    #screen settings
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (46, 55, 71)

    #condition to run
    while True:
        # keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # flip == display most recent screen drawn
        pygame.display.flip()

run_game()
