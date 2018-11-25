import sys
import pygame
from models.bullet import Bullet
from models.alien import Alien

# Alien fleet

def create_fleet(settings, screen, aliens):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width

    # Number of aliens horizontal
    available_space_x = settings.screen_width - (2 * alien_width)
    number_aliens_x = int (available_space_x / (2 * alien_width))

    # Create row of aliens
    for alien_number in range(number_aliens_x):
        alien = Alien(settings, screen)
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        aliens.add(alien)


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
    # Exit shortcut
    if event.key == pygame.K_q:
        sys.exit()

    # Moves
    elif event.key == pygame.K_RIGHT:
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

def update_screen(settings, ship, screen, bullets, aliens):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # flip == display most recent screen drawn
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    # iterate through the list copy to avoid deleting in a for loop
    for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
