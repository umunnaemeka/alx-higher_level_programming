#!/usr/bin/python3
"""This is a module that containts a class"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self, first_name=""):

        self.first_name = first_name
