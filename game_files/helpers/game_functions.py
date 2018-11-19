import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        # Exit conditions
        if event.type == pygame.QUIT:
            sys.exit()
        # Hold key conditions
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        # Stop holding key conditions
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False



def update_screen(settings, ship, screen):
    screen.fill(settings.bg_color)
    ship.blitme()
    # flip == display most recent screen drawn
    pygame.display.flip()
