#  File: Tower.py

#  Description: Calculate the number of moves it takes to move n disks using 4 needles

#  Student's Name: Dharsan Selvakumar

#  Student's UT EID: ss96967

#  Partner's Name: Collin

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/13/2022

#  Date Last Modified: 10/14/2022

import sys
import math


# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves(n):
    if n <= 2:
        return num_moves3(n)
    else:
        a = math.sqrt(2 * n + 1)
        k = int(n - a + 1)

        # moving k disks can use 4 needles, while using the remaining n-k-1 disks can only use 3 needles because they are bigger
        # you end up moving k number of disks twice, and moving n-k-1 numbers of disks twice as well
        total = 2 * num_moves(k) + 2 * num_moves3(n - k - 1) + 1
        return total


# number of moves it takes if you have only 3 needles
def num_moves3(n):
    return 2 ** n - 1


def main():
    # read number of disks and print number of moves
    for line in sys.stdin:
        line = line.strip()
        num_disks = int(line)
        print(num_moves(num_disks))


if __name__ == "__main__":
    main()
