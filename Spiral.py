# given dimensions of square and some numbers to check

# ex for 11, create 11x11 square spiraling from 1 in the center
# upper right hand corner index is (0, 11) and has value of 11^2 = 11
# fill in that outer square by going left then down then right then up
# next square is 9x9 and has index of (1, 9) with value of 81
# top right corners of squares:
# 121 (0,10)
# 81 (1, 9)

# 49 (2, 8)
# 25 (3, 7)
# 9 (4, 6)
# 1 (5, 5)

# 11x11 has 6 squares
# 5x5 has 3 squares
# 7x7 has 4 squares
# num_squares = (dimension // 2) + 1

import math
import sys


def create_spiral(n):
    n = int(n)
    if n % 2 == 0:
        n += 1

    num_squares = (n // 2) + 1
    square = [[0] * n for i in range(n)]  # creates empty square

    top_right = n - 1
    num_to_square = n
    for i in range(num_squares):
        square[i][top_right] = (num_to_square ** 2)

        current_val = num_to_square ** 2
        for j in range(num_to_square - 1):
            square[i][top_right - j] = current_val
            current_val -= 1

        # current_val += 1
        left = top_right - num_to_square + 1
        for k in range(num_to_square - 1):
            square[left + k][i] = current_val
            current_val -= 1
        # current_val += 1
        for l in range(num_to_square - 1):
            square[top_right][i + l] = current_val
            current_val -= 1
        # current_val += 1
        for m in range(num_to_square - 1):
            square[top_right - m][top_right] = current_val
            current_val -= 1

        top_right -= 1
        num_to_square -= 2

    return square


def sum_adjacent_numbers(spiral, n):
    dimension = len(spiral)  # this is okay since it's a square

    r = 0
    c = 0

    for i in range(dimension):
        for j in range(dimension):
            if spiral[i][j] == n:
                r = i
                c = j
                break
    sum = 0
    if r - 1 >= 0 and c - 1 >= 0:
        sum += spiral[r - 1][c - 1]
    if (r - 1 >= 0):
        sum += spiral[r - 1][c]
    if (r - 1 >= 0 and c + 1 <= 10):
        sum += spiral[r - 1][c + 1]
    if (c - 1 >= 0):
        sum += spiral[r][c - 1]
    if (c + 1 <= 10):
        sum += spiral[r][c + 1]
    if (r + 1 <= 10 and c - 1 >= 0):
        sum += spiral[r + 1][c - 1]
    if (r + 1 <= 10):
        sum += spiral[r + 1][c]
    if (r + 1 <= 10 and c + 1 <= 10):
        sum += spiral[r + 1][c + 1]
    return sum


def main():
    dimension = sys.stdin.readline()
    dimension = dimension.strip()
    print(dimension)
    #print(type(dimension))
    #dimension = int(dimension)
    #spiral = create_spiral(dimension)
    nums_to_read = sys.stdin.readlines()


    for num in nums_to_read:
        num = num.strip()
        num = int(num)
        #print(sum_adjacent_numbers(spiral, num))


if __name__ == "__main__":
    main()
