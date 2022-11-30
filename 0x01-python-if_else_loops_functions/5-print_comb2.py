#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i != 9 or j != 9):
            print("{i}{j}, ".format(i=i, j=j), end="")
        else:
            print("{i}{j}\n".format(i=i, j=j), end="")
