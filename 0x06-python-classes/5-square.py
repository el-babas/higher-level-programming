#!/usr/bin/python3
class Square:
    """ Object Square [class]
    """
    def __init__(self, size=0):
        """ Method - Initialize.
        Parameters:
        self -- this class
        size -- size of the square
        """
        self.size = size

    def area(self):
        """ Method - Returns the current square area.
        Parameters:
        self -- this class
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method - prints in stdout the square with the character #
        """
        if self.__size:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()

    @property
    def size(self):
        """ Get - instance attribute size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Set - instance attribute size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
