#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
r_num = number
if (number < 0):
    number = number * -1
result = number % 10
if (result < 6 and result != 0 or r_num < 0):
    message = "and is less than 6 and not 0"
if (result > 5):
    message = "and is greater than 5"
elif (result == 0):
    message = "and is 0"
if (r_num < 0):
    result *= -1
print("Last digit of", r_num,"is", result, message)
