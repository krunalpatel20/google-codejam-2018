#!/usr/bin/env python

T = 3
N = [2, 3, 9]
weights = [[] for i in range (0, T)]
weights[0] = [9, 1]
weights[1] = [8, 4, 100]
weights[2] = [10, 10, 10, 10, 10, 10, 10, 10, 100]

def find_max_level(height, weights):
    if len(weights) <= 0:
        return height
    else:
        height = height + 1
        return find_max_level(height, weights[1:])


print(find_max_level(0, weights[2]))
