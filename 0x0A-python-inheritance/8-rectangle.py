#!/usr/bin/python3
"""
Module 8-rectangle.py
Defines a class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.
        Arguments:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns the formatted string representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


