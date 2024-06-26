#!/usr/bin/python3
"""Define a Square."""


class Square:
    """This is a class representing a square."""

    def __init__(self, size):
        """
        Initialize a Square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
