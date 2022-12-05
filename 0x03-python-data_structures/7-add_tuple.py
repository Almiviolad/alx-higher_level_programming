#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    zero_tuple = (0,)
    while (len(tuple_a) < 2):
        tuple_a = tuple_a + zero_tuple
    while (len(tuple_b) < 2):
        tuple_b = tuple_b + zero_tuple
        res_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return(res_tuple)
