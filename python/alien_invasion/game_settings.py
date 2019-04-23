class GameSettings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen = {
            'width': 1200,
            'height': 800,
            'bg_color': (230, 230, 230)
        }

        # Ship settings
        self.ship = {
            'image': 'images/ship.bmp',
            'speed': 1.5
        }

        # Alien settings
        self.alien = {
            'image': 'images/alien.bmp',
            'speed': 1
        }

        # Bullet settings
        self.bullet = {
            'speed': 1,
            'width': 3,
            'height': 15,
            'color': (60, 60, 60),
            'max_allowed': 3
        }
