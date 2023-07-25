#  File: Work.py

#  Description:

#  Student Name: Dharsan Selvakumar

#  Student UT EID: ss96967

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/28/22

#  Date Last Modified: 9/28/22

import sys, time


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
    # use linear search here
    # want to loop through every possible value of v
    for i in range(1, n):
        if num_lines(i, k) >= n:  # if Vyasa writes at least the necessary amount of lines before sleeping
            v = i  # initial number of lines equals the v value
            break
    if n < 10:
        # since k is between 0 and 10, a n value below 10 will return 0 in after the first coffee
        # that is why n is the number of lines to write before a coffee
        return n
    else:
        return v

    # input: int v, int k, representing a theoretical starting value v with productivity factor k
    # output: an int representing the number of lines of code written using this combination of v and k


# helper function to find the final v value, the total number of lines of code written
def num_lines(v, k):
    # Vyasa has already wrote v lines of code
    lines = v
    factor = k
    # need to start off with the exponent being 1
    exponent = 1

    # want to find number of lines of code finished before he falls asleep
    while (v // k ** exponent) > 0:
        lines = lines + v // k ** exponent
        exponent += 1

    return lines


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def binary_search(n: int, k: int) -> int:
    # use binary search here
    low = 1
    high = n
    mid = (low + high) // 2
    while low != mid:

        if num_lines(mid, k) >= n:
            high = mid
        elif num_lines(mid, k) < n:
            low = mid

        # reset middle
        mid = (low + high) // 2

    #if v is equal to the middle value
    if num_lines(mid, k) < n:
        mid = mid + 1

    if n < 10:
        # since k is between 0 and 10, a n value below 10 will return 0 in after the first coffee
        # that is why n is the number of lines to write before a coffee
        return n
    else:
        return mid


# main has been completed for you
# do NOT change anything below this line
def main():
    num_cases = int((sys.stdin.readline()).strip())

    for i in range(num_cases):
        inp = (sys.stdin.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
