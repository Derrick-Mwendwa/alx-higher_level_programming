#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    weighted_sum = 0
    total_weight = 0

    for tuple in my_list:
        weighted_sum += (tuple[0] * tuple[1])
        total_weight += tuple[1]

    return (weighted_sum / total_weight)
