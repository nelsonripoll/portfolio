import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, alien_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.settings = alien_settings

        self.image = pygame.image.load(alien_settings['image'])
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
