#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for c in str:
        if ord(c) in range(97, 123):
            new_str = new_str + chr(ord(str(c)) - 32)
        else:
            new_str = new_str + c
    print(new_str)
    