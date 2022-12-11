#!/usr/bin/python3
def best_score(a_dictionary):
    max_name = None
    if (a_dictionary == {}):
        return max_name
    for i in a_dictionary:
        max = a_dictionary[i]
        break
    for i in a_dictionary:
        if (a_dictionary[i] > max):
            max = a_dictionary[i]
            max_name = i
    return max_name
