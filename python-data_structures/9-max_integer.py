#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_val = my_list[0]
    for x in my_list[1:]:
        if x > max_val:
            max_val = x
    return max_val
