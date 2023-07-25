import sys


def countPaths(n):
    if n < 3:
        return 1
    elif n < 7:
        return n - 1
    elif n < 15:
        return 2 * n - 7
    elif n < 31:
        return 3 * n - 21
    elif n < 63:
        return 4 * n - 51


if __name__ == '__main__':
    n = int(input())
    print(countPaths(n))
