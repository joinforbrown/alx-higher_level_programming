#!/usr/bin/python3
"""Module that defines a Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a Square instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Compute the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

