import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1
            elif event.key == pygame.K_LEFT:
                ship.rect.centerx -= 1


# elif event.type == pygame.KEYDOWN:
# ➋             if event.key == pygame.K_RIGHT:
#                    # Move the ship to the right.
# ➌                 ship.rect.centerx += 1


def update_screen(settings, ship, screen):
    screen.fill(settings.bg_color)
    ship.blitme()
    # flip == display most recent screen drawn
    pygame.display.flip()