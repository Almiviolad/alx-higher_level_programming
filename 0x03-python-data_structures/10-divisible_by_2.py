#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
         new_list.append(i % 2)
    return (new_list)

my_list = [2, 4, 5]
new_list = divisible_by_2(my_list)
print(new_list)
