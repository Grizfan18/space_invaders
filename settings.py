import pygame

class Settings():
    """A class to store settings for Space Invaders"""

    def __init__(self):
        """Initialize the game settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.image = pygame.image.load('images/Nebula Blue.png')

        # Ship Settings
        self.ship_speed_factor = 3

        #Bullet Settings
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (220,20,60)
