#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implented")
    
    def integer_validator(self, name, value):
        """validate a parameter as an integer.

        Args:
           name (str): The name of the parameter.
           value (int): the parameter to integer.

           Args:
               name (str): The name of the parameter.
               value (int): The parameter to vlidate.
            Raise:
                 Typeerror: If value is not an integer.
                 valueError: If value is <= 0.
            """
            if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0". format(name))

