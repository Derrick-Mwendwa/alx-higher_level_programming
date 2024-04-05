#!/usr/bin/python3
"""Define a Node and a SinglyLinkedList."""


class Node:
    """This is a class representing a node."""

    def __init__(self, data, next_node=None):
        """
        Initialize a Node.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This is a class representing a singly linked list."""

    def __init__(self):
        """Initialize a singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a node into the singly linked list.

        Args:
            value (int): The value of the node.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Return a string representation of the singly linked list."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
