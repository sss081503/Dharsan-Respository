#  File: Triangle.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import sys
from timeit import timeit


# returns the greatest path sum using exhaustive search
def brute_force(grid):

    return


# returns the greatest path sum using greedy approach
def greedy(grid):
    return


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    # base case is when current row = # of rows in 2d list
    # if not base case, then add number either directly below or below and right
    sum = int(grid[0][0])
    final_sum = divide_conquer_helper(0, 0, sum, grid)
    return final_sum


def divide_conquer_helper(starting_row, starting_col, sum, grid):
    # print("Current starting row", starting_row)
    # print('Grid Length', len(grid) - 1)
    if starting_row == len(grid) - 1:
        # print("Sum", sum)
        return sum
    elif grid[starting_row + 1][starting_col] > grid[starting_row + 1][starting_col + 1]:
        sum += grid[starting_row + 1][starting_col]
        return divide_conquer_helper(starting_row + 1, starting_col, sum, grid)
    elif grid[starting_row + 1][starting_col] < grid[starting_row + 1][starting_col + 1]:
        sum += grid[starting_row + 1][starting_col + 1]
        return divide_conquer_helper(starting_row + 1, starting_col + 1, sum, grid)
    else:
        num1 = grid[starting_row + 2][starting_col]
        num2 = grid[starting_row + 2][starting_col + 1]
        num3 = grid[starting_row + 2][starting_col+2]
        max_num = 0
        max_num += max(num1, num2, num3)

        if max_num == num1:
            sum += grid[starting_row + 1][starting_col] + num1
            return divide_conquer_helper(starting_row + 2, starting_col, sum, grid)
        elif max_num == num2:
            sum += grid[starting_row + 1][starting_col] + num2
            return divide_conquer_helper(starting_row + 2, starting_col + 1, sum, grid)
        else:
            sum += grid[starting_row + 1][starting_col+1] + num3
            return divide_conquer_helper(starting_row + 2, starting_col + 2, sum, grid)


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    #create empty grid
    new_grid = []
    n = len(grid)
    for i in range(n):
        new_grid.append([0] * (i+1))

    #dynamic programming
    for i in range(n-1, -1, -1):
        for j in range(len(grid[i])):
            if i == len(new_grid) - 1:
                new_grid[i][j] = grid[i][j]
            else:
                if j == len(grid[i]) - 1:
                    new_grid[i][j] = grid[i][j] + new_grid[i + 1][j]
                else:
                    new_grid[i][j] = grid[i][j] + max(new_grid[i + 1][j], new_grid[i + 1][j + 1])
    return new_grid[0][0]









# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()


    # check that the grid was read in properly
    print (grid)


    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
    times = times / 10
    # print time taken using exhaustive search

    # output greatest path from greedy approach
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
    times = times / 10
    # print time taken using greedy approach

    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    # print time taken using divide-and-conquer approach

    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    # print time taken using dynamic programming


if __name__ == "__main__":
    main()
