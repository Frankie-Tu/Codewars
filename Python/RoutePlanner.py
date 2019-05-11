"""
Codewars Challenge created by g964
write a function route_planner(t, k, ls):
t : max travel distance
k:  number of towns to visit.
ls : list of towns in distance value, format: [21,23,32,42]
Find the max possible travel distance to k towns up until the max distance of t
"""
from itertools import combinations


def route_planner(t, k, ls):
    # check if we have enough towns to visit
    if len(ls) < k:
        return None
    else:
        # find all combinations
        all_combinations = combinations(ls, k)
        current_sum = 0
        # check sum of all combinations
        for combination in all_combinations:
            if current_sum < sum(combination) <= t:
                current_sum = sum(combination)
        # if it is not possible to visit the number of towns required under the maxium distance allowed
        if current_sum == 0:
            return None
        else:
            return current_sum


# Test
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(route_planner(430, 5, xs))