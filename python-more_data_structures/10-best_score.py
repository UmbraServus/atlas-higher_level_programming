#!/usr/bin/python3
def best_score(a_dictionary):
    result = 0
    tmp_key = None
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > result:
            result = value
            tmp_key = key
    return tmp_key
