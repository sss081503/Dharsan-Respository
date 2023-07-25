# Description: Determine if a string of brackets is organized legally.
# Student Name: Dharsan Selvakumar
# Student UT EID: ss96967
# Course Name: CS 313E
# Unique Number: 52535
# Input: any valid string
# Output: the string "true" if it is valid, "false" if is not
import sys


def valid(s):
    # TODO: Implement me!
    # temporary, change return when writing code
    if len(s) % 2 == 1:
        return 'false'
    else:
        bracket_dict = {'{': 0, '}': 0, '[': 0, ']': 0, '(': 0, ')': 0}

        # if there are the same number of opening brackets of one type as the closing brackets of the same type, return true
        for i in range(len(s)):
            bracket_dict[s[i]] += 1  # count the number of instances of that bracket

        # if the number of instances of closing and opening brackets of same type are the same
        if bracket_dict['{'] == bracket_dict['}'] and bracket_dict['['] == bracket_dict[']'] and bracket_dict['('] == \
                bracket_dict[')']:
            return 'true'
        else:
            return 'false'


def main():
    # read the input file from stdin
    string = sys.stdin.readline().strip()
    print(valid(string))


# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
