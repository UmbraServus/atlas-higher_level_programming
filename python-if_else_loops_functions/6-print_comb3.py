#!/usr/bin/python3
for fd in range(9):
    for sd in range(0 + 1, 10):
                if fd == 8 and sd == 9:
                       print(f"{fd}{sd}")
                else:
                        print(f"{fd}{sd}", end=", ")
                        