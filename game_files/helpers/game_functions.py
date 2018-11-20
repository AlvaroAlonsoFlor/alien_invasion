import sys
import pygame
from models.bullet import Bullet


def check_events(ship, settings, screen, bullets):
    for event in pygame.event.get():
        # Exit conditions
        if event.type == pygame.QUIT:
            sys.exit()
        # Hold key conditions
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, screen, settings, bullets)
        # Stop holding key conditions
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship, screen, settings, bullets):
    # Moves
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    
    # Bullets
    fire_bullets(event, ship, screen, settings, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False

def fire_bullets(event, ship, screen, settings, bullets):
    if event.key == pygame.K_SPACE and len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)



# UPDATE

def update_screen(settings, ship, screen, bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # flip == display most recent screen drawn
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    # iterate through the list copy to avoid deleting in a for loop
    for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                        bullets.remove(bullet)
