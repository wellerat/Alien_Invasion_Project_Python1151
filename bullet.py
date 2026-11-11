"""
Program: bullet.py

Purpose:  Defin the Bullet class and mange projectice creation, 
          movement, and behavior for the game's standard, double
          and spread-shot weapon systems.
          
Author: Ann Cooper

Starter Code: Python Crash Course, 3rd Edition by Eric Matthes

Date Created: 10/22/26
Date Updated: 11/10/26
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to mangage bullets fired from teh ship."""
    def __init__(self,ai_game, dx=0):
        """Create a bulled object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.dx = dx

        # Create a bullet rect at (0, _) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update teh exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

        self.rect.x +=self.dx

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)