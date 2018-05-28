import pygame

class Settings():
    """A class to store settings for Space Invaders"""

    def __init__(self):
        """Initialize the game settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800

        #Background settings
        self.image = pygame.image.load('images/Nebula Blue.png')
        self.image_y = 0
        self.background_speed = 1

        # Ship Settings
        self.ship_speed_factor = 5

        # Alien settings
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 15
        # fleet direction: 1 = right, -1 = left
        self.fleet_direction = 1

        #Bullet Settings
        self.bullet_speed_factor = 15
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (220, 20, 60)
        self.bullets_allowed = 15
