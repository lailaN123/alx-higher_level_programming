#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if x != 8 or y != 9:
            if x != y and x < y:
                print("{}{}, ".format(x, y), end="")
        else:
            print("{}{}".format(x, y))