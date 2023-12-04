#!/usr/bin/python3
"""
it contains MyList class
"""


class MyList(list):
    """Subclass of list"""
    def __init__(self):
        """initializes object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
