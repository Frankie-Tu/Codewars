def Missing_Array_Length(array_of_arrays):
    """
    level : 6 kyu
    Challenge: if you sort the arrays by length,
    their length values should be consecutive,
    find the missing one.

    when array_of_arrays or array inside the array_of arrays is empty/null,
    return 0
    """
    # check if array or an array inside array_of_arrays is empty
    if not array_of_arrays or [] in array_of_arrays or None in array_of_arrays:
        return 0
    
    # convert arrays to their length values
    array_length = list(map(lambda x: len(x), array_of_arrays))

    # find missing length value
    for num in range(min(array_length),max(array_length)):
        if num not in array_length:
            return num


Missing_Array_Length([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]) == 3
Missing_Array_Length([[1, 2], [4, 5, 1, 1], [], [5, 6, 7, 8, 9]]) == 0
