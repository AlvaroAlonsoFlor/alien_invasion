import sys
import pygame
from models.bullet import Bullet
from models.alien import Alien
from time import sleep

# ALIEN FLEET

def create_fleet(settings, screen, aliens, ship): 

    total_rows = get_number_of_rows(settings, screen, ship)

    for row_number in range(total_rows):  
        create_alien_row(settings, screen, aliens, row_number)
    

def create_alien_row(settings, screen, aliens, row_number):

    # Get number of aliens
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    x_aliens = get_number_of_aliens_x(settings, alien_width)

    for alien_number in range(x_aliens):
        alien = Alien(settings, screen)
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)

def get_number_of_aliens_x(settings, alien_width):
    available_space_x = settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x

def get_number_of_rows(settings, screen,  ship):

    # Get alien and ship height

    alien = Alien(settings, screen)
    alien_height = alien.rect.height

    ship_height = ship.rect.height

    # Calculate number of rows

    available_space_y = settings.screen_height - (3 * alien_height) - ship_height
    number_of_rows = int(available_space_y / (2 * alien_height))

    return number_of_rows

# Limit checkers

def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.is_over_edge():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1
 

# EVENTS

def check_events(ship, settings, screen, bullets, play_button, game_state):
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
        # Check if clicked in play
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_state, play_button, mouse_x, mouse_y)


def check_play_button(game_state, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
           game_state.game_active = True

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

def check_alien_bottom(settings, game_state, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            return True


def ship_hit(game_state, aliens, bullets, screen, ship, settings):

    if game_state.ships_left:
        game_state.ships_left -= 1

        #Clear aliens and bullets
        aliens.empty()
        bullets.empty()

        # Recreate position and enemies
        create_fleet(settings, screen, aliens, ship)
        ship.recenter()

        # Pause
        sleep(1)
    else:
        game_state.game_active = False
        
    

# UPDATE

def update_screen(settings, ship, screen, bullets, aliens, game_state, play_button):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not game_state.game_active:
        play_button.draw_button()

    # flip == display most recent screen drawn
    pygame.display.flip()

   

def update_bullets(bullets, aliens):
    bullets.update()

    # If it hits an alien, delete bullet and alien
    pygame.sprite.groupcollide(bullets, aliens, True, True)

    # iterate through the list copy to avoid deleting in a for loop
    for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)

def update_aliens(settings, aliens, ship, game_state, screen, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()

    # Hits player
    if pygame.sprite.spritecollideany(ship, aliens) or check_alien_bottom(settings, game_state, screen, ship, aliens, bullets):
        ship_hit(game_state, aliens, bullets, screen, ship, settings)
