#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry'). Basegeometry

class Rectangle(Basegeometry):
    """Represent a rectangle using Basegeometry."""
    def __int__(self. width, height):
        """Intialize a new rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new rectangle.
        """
        self.integer_validator("width". width)
        self.__width = width
        self.integer-validator("height". height)
        self.__height = height
