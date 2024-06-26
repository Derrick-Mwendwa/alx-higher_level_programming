#!/usr/bin/python3
"""Define a MagicClass."""


import math


class MagicClass:
    """This is a class representing a circle."""

    def __init__(self, radius=0):
        """
        Initialize a circle.

        Args:
            radius (int or float): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the circle."""
        return (2 * math.pi * self.__radius)
