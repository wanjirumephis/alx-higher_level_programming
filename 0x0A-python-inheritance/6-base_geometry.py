#!/usr/bin/python3
""" creating a class """


class BaseGeometry:
    """Using the object class as the base class"""
    def area(self):
        raise Exception("area() is not implemented")
