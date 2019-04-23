import pygame
import time
import game_functions as gf

from game_settings import GameSettings
from ship          import Ship
from pygame.sprite import Group

def run_game():
    pygame.init()
    gs      = GameSettings()
    screen  = gf.create_screen(gs.screen)
    ship    = Ship(gs.ship, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(gs, screen, ship, aliens)

    while True:
        gf.check_events(gs, screen, ship, bullets, time)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(gs.screen, screen, ship, aliens, bullets)

run_game()
