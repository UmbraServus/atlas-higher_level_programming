#!/usr/bin/python3
""" Module: class Mylist along with methods and objects associated with it. """


class MyList(list):
    """ class Mylist that inherits from list """

    def print_sorted(self):
        """ prints list in sorted ascending order

            args:
                self

            Examples:
                >>> my_list = Mylist([1, 4, 2, 3, 5])
                >>> my_list.print_sorted()
                [1, 2, 3, 4, 5]
        """
        sorted_list = sorted(self)
        print(sorted_list)
