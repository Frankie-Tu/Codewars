"""
Original challenge posted by JKphobic on Codewars.com
You arrived appointment 10 mins earlier.
You decide to talk a walk in [n,s,e,w] directions
You only walk a single block each minute and it is always the same length
Write a function to verify if you take exactly 10 mins and come back to the starting point by the end of the walk

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only).
It will never give you an empty array (that's not a walk, that's standing still!).
"""

# my verified solution
def isValidWalk(walk):
    # coordinates
    start_position = [0, 0]
    for item in walk:
        if item == 'n':
            start_position[1] += 1
        elif item == 's':
            start_position[1] -= 1
        elif item == 'e':
            start_position[0] += 1
        elif item == 'w':
            start_position[0] -= 1

    return start_position == [0, 0] and len(walk) == 10