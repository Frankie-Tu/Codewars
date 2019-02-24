"""
Example:

solution('XXI') # should return 21
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""

def solution(roman):
    converter = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}
    # initializing values
    result = 0
    index = 0
    while index < len(roman):
        # when current character is not the last one
        if index != len(roman) - 1:
            # if the next character is smaller than the current, add current to result
            if converter[roman[index]] >= converter[roman[index + 1]]:
                result += converter[roman[index]]
                index += 1
            # otherwise add (next number value - current number value) to result
            else:
                result += converter[roman[index + 1]] - converter[roman[index]]
                # increment by 2 to skip next character
                index += 2
        else:
            result += converter[roman[index]]
            index += 1
    return result

print(solution("VI"))
print(solution("IV"))
print(solution("XXI"))

