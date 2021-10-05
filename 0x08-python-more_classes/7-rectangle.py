#!/usr/bin/python3
'''An rectangle class'''


class Rectangle():
    '''
    A rectangle class
    Attributes:
        number_of_instances: int
        print_symbol: str
    Args:
        width: An integer greater than -1
        height: An integer greater than -1
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''init method'''
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the reactangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returs the perimeter of the rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns the rectangle with the print_symbol character."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Returns the string representation of the Rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Print a message for every deletion of
        the rectangle.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
