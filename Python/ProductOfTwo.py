"""
Original challenge proposed by Codewars user g964

Given a sequence of number from 1 to N where N > 0

Find the the two numbers a , b in the sequence where the 
the product of a and b equals the sum of all numbers excluding a and b.

Return [(a,b),(b,a)]

if not possible return []

example product_of_two(26)
returns [(15, 21), (21, 15)]
15 * 21 = 315
numbers in range 1 to 26 excluding 15 and 21 sum up to 315
"""

from itertools import combinations
import timeit

# first iteration, #O(n^3)
def product_of_two(n):
    # python range goes up to but not including the upper bound, thus +1
    num_seq = list(range(1, n+1))

    # find all [a,b] combinations from the sequence, O(n^2), two loops in combinations function
    all_combinations = combinations(num_seq, 2)

    result = []
    # filter out selected number a, b from the list and do sum
    # and check if a * b equals that sum, O(n^2), one combination loop, one more loop in sum
    for combination in all_combinations:
        if combination[0]*combination[1] == sum(list(filter(lambda x: x not in combination ,num_seq))):
            result.extend([(combination[0], combination[1]), (combination[1], combination[0])])
    return sorted(result, key=lambda x: x[0])

# much more efficient algorithm, O(n)
def product_of_two2(n):
    # python range goes up to but not including the upper bound, thus +1
    num_seq = list(range(1, n+1))

    # gauss's formula
    # 1 2 3 4 5
    # 5 4 3 2 1
    # ---------
    # 6 6 6 6 6
    # / / / / /
    # 2 2 2 2 2
    # = = = = =
    # 3 3 3 3 3 (15)
    num_seq_sum = (num_seq[0] + num_seq[-1]) * len(num_seq) / 2
    
    result = []
    for a in num_seq:
        # b can only be smaller than n
        if num_seq_sum / a < n:
            # round down
            b = int(((num_seq_sum - a) / a))
            if a * b == (num_seq_sum - a - b):
                result.extend([(b,a),(a,b)])

    return sorted(result, key=lambda x: x[0])

# 0.060743096999431145s
print(timeit.timeit("product_of_two(100)", "from __main__ import product_of_two", number=1))

# 3.9660999391344376e-05s
print(timeit.timeit("product_of_two2(100)", "from __main__ import product_of_two2", number=1))

# 53.601970453999456s
print(timeit.timeit("product_of_two(1000)", "from __main__ import product_of_two", number=1))

# 0.00021786900106235407
print(timeit.timeit("product_of_two2(1000)", "from __main__ import product_of_two2", number=1))