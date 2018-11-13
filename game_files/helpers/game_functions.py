import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, ship, screen):
    screen.fill(settings.bg_color)
    ship.blitme()
    # flip == display most recent screen drawn
    pygame.display.flip()