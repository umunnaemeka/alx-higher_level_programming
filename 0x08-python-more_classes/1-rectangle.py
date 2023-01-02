#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """The Rectangle class"""
    def ___init___(self, width=0, height=0):
        self.height = height
        self.height = width

    @property
    def width(self):
        return self.___width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.___width = value

        @property
        def height(self):
            return self.___height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError( "height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")

            self.___height = value
            
