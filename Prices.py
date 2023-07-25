# File: Prices.py
# Student Name: Dharsan Selvakumar
# Student UT EID: ss96967
# Course Name: CS 313E
# Unique Number: 52535
import sys

# Input: prices is a list of integers
# Output: weeks is a list of integers representing the number of weeks you need to wait for
from typing import List


def compute_weeks(prices):
    weeks = [] #initialize the list
    for i in range(len(prices)): #loop through the all the prices
        #initialize a count variable that counts the number of iterations to get to a value greater than
        #the current value
        count = 0

        #if the index is at the last value, append 0
        if i == len(prices) - 1:
            weeks.append(0)
            return weeks

        #otherwise, count how many indices it takes to get to a value bigger than the current value
        else:
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    count = j - i
                    break

            #append the count
            weeks.append(count)
    return weeks


def main():
    # read the input file from stdin
    line = sys.stdin.readline().strip()
    # convert string to a list of integers
    prices = [int(v) for v in line.split()]
    weeks = compute_weeks(prices)
    weeks_str = ' '.join([str(v) for v in weeks])
    print(weeks_str)


# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
