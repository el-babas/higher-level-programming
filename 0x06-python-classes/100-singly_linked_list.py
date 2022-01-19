#!/usr/bin/python3
""" Define an objects.
"""


class Node:
    """ Object Node [class]
    """
    def __init__(self, data, next_node=None):
        """ Method - Initialize.

        Args:
            self (this): This class.
            data (int): The value of the Node.
            next_node (Node): The value of the next Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Get - Instance attribute data.
        """
        return (self.__data)

    @property
    def next_node(self):
        """ Get - Instance attribute next_node.
        """
        return (self.__next_node)

    @data.setter
    def data(self, value):
        """ Set - Instance attribute data.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """ Set - Instance attribute next_node.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Object SinglyLinkedList [class]
    """
    def __init__(self):
        """ Method - Initialize.

        Args:
            self (this): This class.
        """
        self.__head = None

    def __str__(self):
        """ Method - Print this object

        Args:
            self (this): This class.
        """
        pstr = ""
        temp = self.__head
        while temp is not None:
            pstr += str(temp.data)
            if temp.next_node is not None:
                pstr += "\n"
            temp = temp.next_node
        return (pstr)

    def sorted_insert(self, value):
        temp = self.__head
        while temp is not None:
            if temp.data > value:
                break
            temp_prev = temp
            temp = temp.next_node

        new_node = Node(value, temp)
        if temp == self.__head:
            self.__head = new_node
        else:
            temp_prev.next_node = new_node
