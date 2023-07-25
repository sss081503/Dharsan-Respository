# File: Pattern.py
# Description:
# Student Name: Dharsan Selvakumar
# Student UT EID: ss96967
# Course Name: CS 313E
# Unique Number: 52535
import sys


# helper function
def pal(s):  # checking if s is a palindrome
    # base case
    if s == "":
        return True
    # base case with one character
    if len(s) == 1:
        return True

    # recursive call by comparing outer characters
    elif s[0] == s[len(s) - 1]:
        return pal(s[1:(len(s) - 1)])
    else:
        return False


# obtained this code from what we learned in lecture
# helper function to find subsets
def sub_sets(a, b, i, list_subsets):
    # high is equal to the length of list a
    high_val = len(a)

    if i == high_val:  # if index is equal to the high_val

        list_subsets.append(b)
        return
    else:  # otherwise create a new substring list and recursively call subsets
        new = b[:]  # create new list

        b.append(a[i])

        # calling sub_sets twice on two different recursive calls with b and new
        sub_sets(a, b, i + 1, list_subsets)
        sub_sets(a, new, i + 1, list_subsets)


def proper_substring(s, k):
    list_s = list(s)  # turn s into a list

    # initialize subsets
    subsets = []

    # call sub_sets helper function
    sub_sets(list_s, [], 0, subsets)

    # create new list to store final subsets
    fin_subs = []

    # loop through subsets and append to final subsets
    for idx in range(len(subsets)):
        diff = len(s) - k  # find difference

        # if the length of that subset is equal to the difference
        if len(subsets[idx]) == diff:
            fin_subs.append(subsets[idx])

    # want to see if all final subsets are palindromes or not
    for subset in fin_subs:

        string = ''  # create an empty string

        # adding the characters of the subset to the string
        for char in subset:
            string = string + char

        # checking if the string is a palindrome
        if pal(string):
            return True

    # if some are not palindromes
    return False


# TAKE CAUTION TO EDIT BELOW THIS LINE
def main():
    s = sys.stdin.readline().strip()
    k = int(sys.stdin.readline())
    print(proper_substring(s, k))


if __name__ == "__main__":
    main()
