#!/usr/bin/python3
def uniq_add(my_list=[]):
    myset = set(my_list)
    return sum(x for x in myset)
