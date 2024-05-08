#!/usr/bin/python3
import sys
if __name__ == "__main__":
    index = 1
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
            print("1 argument:\n1: {}".format(sys.argv[1]))
    else:
        print("{} arguments".format(len(sys.argv) - 1))
        for i in sys.argv[1:]:
            print("{}: {}".format(index, i))
            index+= 1
