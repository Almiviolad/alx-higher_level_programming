#!/usr/bin/python3
def best_score(a_dictionary):
    for i in a_dictionary:
        max = a_dictionary[i]
        break
    for i in a_dictionary:
        if (a_dictionary[i] > max):
            max = a_dictionary[i]
    return max
