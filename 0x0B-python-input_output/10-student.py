#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Class representing a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the student instance"""
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict
