"""
Program: arsenal.py

Purpose:  Manage the player's available weapons.  Track the currently
          selected weapon.
          
Auhor:  Ann Cooper

Starter Code: Python Crash Course, 3rd Edition by Eric Matthes

Date Created: 11/10/26
Date Updated: 11/10/26
"""

class Arsenal:
    """Track the player's currently selected weapon."""

    def __init__(self):
        """Initialize the arsenal"""
        self.current_weapon = "Standard"