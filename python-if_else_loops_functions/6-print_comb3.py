#!/usr/bin/python3
for fd in range(0, 10):
    for sd in range(fd + 1, 10):
        if fd == 8 and sd == 9:
            print("{}{}".format(fd, sd))
        elif fd != sd:
            print("{}{}".format(fd, sd), end=", ")