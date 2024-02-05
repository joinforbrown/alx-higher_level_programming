#!/usr/bin/python3

""" Module - 9-rectangle """

class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """
        Raise an exception with an error message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class, inheritance from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Constructor
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Square class, inheritance from Rectangle
    """
    def __init__(self, size):
        """
        Constructor
        """
        super().__init__(size, size)

