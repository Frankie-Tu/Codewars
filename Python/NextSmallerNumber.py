'''
Given a random positive integer value.
Return the next smaller number with the same digits, if no such number, return -1
Returned number should not start with 0

logic:

input -> int = 65123
turn input to int array -> int_arr = [6,5,1,2,3]

starting from the last digit, find when the array is no longer in ascending order:
[5,1,2,3]
first_half = [6]
swap_num = 5
second_half = [1,2,3]
[first_half] swap_num [second_half] -> [6] 5 [1,2,3]

find the number in the second_half array that is immediately smaller than the swap_num, swap that number with swap_num:
[6] 3 [1,2,5]

sort second_half desc -> [5,2,1]
concatenate everything together -> [6,3,5,2,1]
join the elemens together and change data type to int -> 63521

'''

def next_smaller(num):
    # turn int into array of digits
    num_arr = list(str(num))

    i = len(num_arr) - 1
    first_half = []
    second_half = []

    # starting from the last digit
    while i >= 0:
        current_arr = num_arr[i:]

        # when the array is no longer in ascending order
        if current_arr != sorted(current_arr):
            first_half = num_arr[:i]
            second_half = num_arr[i+1:]
            swap_num = num_arr[i]

            # find the next largest in the second_half that is smaller than swap_num
            for x in reversed(range(int(swap_num))):
                if str(x) in second_half:
                    second_half.append(swap_num)
                    second_half = sorted(second_half,reverse = True)
                    swap_num = str(x)
                    second_half.remove(swap_num)
                    break

            # concatenate [first_half] swap_num [second_half] together
            first_half.append(swap_num)
            first_half.extend(second_half)

            if first_half[0] != "0":
                return int("".join(first_half))
            else:
                return -1
        i -= 1

    # condition was not met 
    return -1


print(next_smaller(65123))