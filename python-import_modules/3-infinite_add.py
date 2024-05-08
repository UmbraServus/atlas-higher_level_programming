#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    if len(sys.argv) == 1:
        print(0)
    else:
        for arg in sys.argv[1:]:
            result += int(arg)
print(result)