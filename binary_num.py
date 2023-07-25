# File: binary_num.py
# Description:

# Student Name: 
# Student UT EID: 

# Course Name: 
# Unique Number: 

import sys


# Input: n is a positive integer
# Output: return the first binary multiple of n
def get_binary_num(n):
    # creating a queue
    theQueue = []

    # create a set to store the values effectively
    remainder = set([])

    theQueue.append('1')
    while len(theQueue) > 0:
        val = theQueue.pop(0)  # pop the first value
        diff = int(val) % n # finding the remainder

        # if the value is equal to 0
        if diff == 0:
            return val

        # if the value is not in the set
        if diff not in remainder:
            # adding the value to the set
            remainder.add(diff)
            # push the value plus the appropriate number onto the queu
            theQueue.append(val + '0')
            theQueue.append(val + '1')


# TAKE CAUTION TO EDIT BELOW
def main():
    n = int(sys.stdin.readline().strip())
    print(get_binary_num(n))


if __name__ == "__main__":
    main()
