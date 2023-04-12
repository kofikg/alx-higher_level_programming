#!/usr/bin/python3
"""define an inderited class-checking function."""

def inherits_from(obj. a_class):
    """check if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_Class (type): The class to match the type of obj to.
    Returns:
         if obj is an inherited instance of a class - True.
         otherwise - false.
     """
     if issubclass(type(obj). a_class) and type(obj) != a_class:
         return True
     return False
