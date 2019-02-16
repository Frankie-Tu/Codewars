"""
Challenge created by user NullData:
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:
i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

eg. parse("iiisdoso")  ==>  [8, 64]
"""

def parse(data):
    current_value = 0
    result_arr = []
    for item in data:
        if item == "i":
            current_value += 1
        elif item == "d":
            current_value -= 1
        elif item == "s":
            current_value = current_value ** 2
        elif item == "o":
            result_arr.append(current_value)

    return result_arr

print(parse("iiisdoso"))