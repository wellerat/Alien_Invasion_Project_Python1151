"""
Program: game_stats.py

Purpose:  Store and manage game state information used throughout the 
          Alien Invasion project.
          
Author: Ann Cooper

Starter Code: Python Crash Course, 3rd Edition by Eric Matthes

Date Created: 10/22/26
Date Updated: 11/10/26
"""
class GameStats:
    """Track statistics for Alien Invation"""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should neve be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1