#!/usr/bin/python3
"""
No module imported
"""


class Square:
    """
    Private instance attribute size
    public instance method
    """
    def __init__(self, size=0):
        """private instance attribute
        parameters
        -------------------------
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """
        self.__size = size

    def area(self):
        """
        public instance method
        returns the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """ 
        to retrieve private instance attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        to set private instance attribute
        """
        if type(value) is not int:
        raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        print squre using #
        """
        printSize = self.__size
        if printSize == 0:
            print()
            for i in range(printSize):
                for j in range(printSize):
                    print("#", end="")
                print()
