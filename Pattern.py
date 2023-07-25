# File: Pattern.py

# Description: Given a sequence of number, find length traveled on number pad

# Student Name: Dharsan Selvakumar

# Student UT EID: ss96967

# Course Name: CS 313E

# Unique Number: 52535

import sys
import math


# Input: a list of integers representing the sequence of numbers traveled, len(ptrn) >= 2
# Output: distance traveled on the number pad
def unlock_pattern(ptrn):
    grid = [[1,2,3,4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    dist = 0
    for i in range(len(ptrn)-1):
        for j in range(4):
            for k in range(4):
                if grid[j][k] == ptrn[i]:
                    row1 = j
                    col1 = k
        for j in range(4):
            for k in range(4):
                if grid[j][k] == ptrn[i+1]:
                    row2 = j
                    col2 = k
        dist = dist + math.hypot(row2-row1, col2-col1)
    return dist
# TAKE CAUTION TO EDIT BELOW THIS LINE
def main():
    line = sys.stdin.readline().split()
    input_pattern = []
    for ele in line:
        input_pattern.append(int(ele))
    print("{:.2f}".format(unlock_pattern(input_pattern)))

if __name__ == "__main__":
    main()
