#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    a = 10
    b = 5
    add_r = add(a, b)
    sub_r = sub(a, b)
    mul_r = mul(a, b)
    div_r = div(a, b)
    print("{} + {} = {}".format(a, b, add_r))
    print("{} - {} = {}".format(a, b, sub_r))
    print("{} * {} = {}".format(a, b, mul_r))
    print("{} /  {} = {}".format(a, b, div_r))
