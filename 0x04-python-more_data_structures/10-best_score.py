#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    b_score = list(a_dictionary.keys())[0]
    large = a_dictionary[b_score]

    for x, y in a_dictionary.items():
        if y > large:
            large = y
            b_score = x

    return b_score
