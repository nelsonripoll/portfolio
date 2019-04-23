import sys
import pygame 

from bullet import Bullet
from alien  import Alien

def create_screen(screen_settings):
    screen = pygame.display.set_mode((screen_settings['width'], screen_settings['height']))
    pygame.display.set_caption("Alien Invasion")
    return screen

def create_fleet(game_settings, screen, ship, aliens):
    alien = Alien(game_settings.alien, screen)
    number_aliens_x = get_number_aliens_x(game_settings.screen, alien.rect.width)
    number_rows = get_number_rows(game_settings.screen, ship.rect.height, alien.rect.height) 

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings.alien, screen, aliens, alien_number, row_number)

def get_number_aliens_x(screen_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = screen_settings['width'] - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(screen_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (screen_settings['height'] - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(alien_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(alien_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def check_events(game_settings, screen, ship, bullets, time):
    """Respond to keypresses and mouse events."""
    print("CHECK EVENTS " + str(time.time()))
    for event in pygame.event.get():
        print("EVENT " + str(time.time()))
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings.bullet, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False 
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False 

def fire_bullet(bullet_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < bullet_settings['max_allowed']:
        new_bullet = Bullet(bullet_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    """Update bullet positions"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(screen_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""
    screen.fill(screen_settings['bg_color'])
    ship.blitme()
    aliens.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()
