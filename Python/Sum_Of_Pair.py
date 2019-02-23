"""
Challenge created by AlejandorLazaro:

Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
"""
import timeit

def sum_pairs(ints, s):
    """
    only the index of the second number matters,
    as long as we can find the difference between s and current number in the list before the second number
    we return the pair
    """
    currentindex = 0
    for num in ints:
        if s - num in ints[0: currentindex]:
            return [s - num, num]
        currentindex += 1
    return None

# better solution
def sum_pairs2(ints, s):
    number_set = set()
    for num in ints:
        if s - num in number_set:
            return [s - num, num]
        else:
            number_set.add(num)
    return None


"""
efficiency testing, confirming that new solution is superior
first solution loops through all the numbers before current number
second solution puts "already seen" numbers into set
"""

# 1.08s
print(timeit.timeit("sum_pairs([10, 5, 2, 3, 7, 5, 25],30)", "from __main__ import sum_pairs", number=1000000))
print(sum_pairs([10, 5, 2, 3, 7, 5, 25], 30))

# 0.8s
print(timeit.timeit("sum_pairs2([10, 5, 2, 3, 7, 5, 25],30)", "from __main__ import sum_pairs2", number=1000000))
print(sum_pairs2([10, 5, 2, 3, 7, 5, 25], 30))

