#!/usr/bin/python3
def print_last_digit(number):
    r_num = number
    if (number < 0):
        number = number * -1
    result = number % 10
    if (r_num < 0):
        result *= -1
    print("{}".format(result), end="")
