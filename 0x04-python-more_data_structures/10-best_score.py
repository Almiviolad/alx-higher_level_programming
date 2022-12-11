#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary == {} or a_dictionary == None):
        return None
    max_name = None
    for i in a_dictionary:
        max = a_dictionary[i]
        break
    for i in a_dictionary:
        if (a_dictionary[i] > max):
            max = a_dictionary[i]
            max_name = i
    return max_name
