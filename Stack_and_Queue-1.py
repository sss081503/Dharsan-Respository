# File: Stack_and_Queue.py

# Description: Choose a fixed number of elements to maximize final result

# Student Name:

# Student EID:

# Course Name: CS 313E

# Unique Number

import sys


# Input: nums is a list of positive integers; tgt is a positive integer indicating how many numbers there should be.
# Output: returns the maximum sum possible of the numbers picked by the rules explained in specifications.
def pop_or_dequeue(nums, tgt):
    leng = len(nums) - tgt

    minimum - float('inf')
    start = 0
    end = leng
    for j in range(len(nums) - k + 1):
        sum1 = sum(nums[i:i+k])
        if sum1 < minimum:
            start = j
            end = j + k
            minimum = sum1

        val = sum(nums[0:start]) + sum(nums[end:])
    return val

# TAKE CAUTION TO EDIT BELOW THIS LINE
if __name__ == "__main__":
    input1 = sys.stdin.readline().split()
    num_list = []
    for ele in input1:
        num_list.append(int(ele))
    num = int(sys.stdin.readline())
    print(pop_or_dequeue(num_list, num))
