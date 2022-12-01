#!/usr/bin/python3
def uppercase(str):
    for i in str:
            if (i >= 65 and i <= 12 and i != 96):
                if (ord(i) >= 97 and ord(i) <= 123):
                    i = ord(i) - 32
                else:
                    i = ord(i)
                print("{:c}".format(i), end="")
    print("\n", end="")
