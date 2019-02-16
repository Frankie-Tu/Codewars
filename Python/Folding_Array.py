"""
task: fold the array n times (one of the Codewars challenge)
example:
array = [1,2,3,4,5], runs = 1 => [1+5,2+4,3] = [6,6,3]
array = [1,2,3,4,5], runs = 2 => [6+3,6] = [9,6]

array = [1,2,3,4], runs = 1 => [1+4,2+3] = [5,5]
and so on ...
"""
def fold_array(array, runs):
    current_run = 0
    while current_run < runs:
        array_len = len(array)
        # temp array
        array_temp = []
        index = 0
        # even array
        if array_len % 2 == 0:
            # loop until mid point (one fold)
            while index < array_len/2:
                array_temp.append(array[index] + array.pop())
                index += 1
            # finished with current run, overwrite original array with content from temp array
            array = array_temp
        # odd array
        else:
            # loop until mid point (one fold), disregard .5
            while index <= array_len//2:
                # if not middle number in the array
                if index != array_len//2:
                    array_temp.append(array[index] + array.pop())
                    index += 1
                else:
                    # append middle number
                    array_temp.append(array[index])
                    index += 1
            array = array_temp
        # current run finished, add 1 to current run count
        current_run += 1

    return array


if __name__ == "__main__":
    # testing
    arr = [1, 2, 3, 4]
    print(fold_array(arr, 2))

