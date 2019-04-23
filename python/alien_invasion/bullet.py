import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from ship."""

    def __init__(self, bullet_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, bullet_settings['width'], bullet_settings['height'])
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = bullet_settings['color']
        self.speed_factor = bullet_settings['speed']

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
