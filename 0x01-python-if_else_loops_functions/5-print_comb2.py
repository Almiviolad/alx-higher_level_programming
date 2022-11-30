#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        print("{i}{j}".format(i = i, j = j), end="")
        if (i != 9 or j != 9):
            print(", ", end="")
        else:
            print("\n",end="")
