#!/usr/bin/python3
for i in range(100):
    if (i != 99):
        print("{}{}, ".format(int(i / 10), i % 10), end="")
    else:
        print("{}{}\n".format(int(i / 10), i % 10))