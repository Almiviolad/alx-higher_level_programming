#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in range(0, len(my_list)):
	new_list[i] = not(my_list[i] % 2)
    return (new_list)
