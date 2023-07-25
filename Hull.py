#  File: Hull.py

#  Description:

#  Student Name: Dharsan Selvakumar

#  Student UT EID: ss96967

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/26/22

#  Date Last Modified:

import sys

import math


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)

    def __ne__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y <= other.y
        return self.x <= other.x

    def __gt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if abs(self.y - other.y) < tol:
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)


# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det(p, q, r):
    determinant = q.x * r.y - r.x * q.y + r.x * p.y - p.x * r.y + p.x * q.y - q.x * p.y
    return determinant


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull(sorted_points):
    upper_hull = []
    for i in range(len(sorted_points)):
        upper_hull.append(sorted_points[i])

    return


# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly(convex_poly):
    determinant = 0
    for i in range(len(convex_poly)-1):
        determinant = determinant + convex_poly[i].x * convex_poly[i+1].y
        determinant = determinant - convex_poly[i].y * convex_poly[i+1].x
    determinant = determinant + convex_poly[-1].x * convex_poly[0].y
    determinant = determinant - convex_poly[-1].y * convex_poly[0].x
    area = 0.5 * math.fabs(determinant)
    return area


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases

    return "all test cases passed"


def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int(line)

    # read data from standard input
    for i in range(num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int(line[0])
        y = int(line[1])
        points_list.append(Point(x, y))

    # sort the list according to x-coordinates
    sorted_points = sorted(points_list)

  '''
  # print the sorted list of Point objects
  for p in sorted_points:
    print (str(p))
  '''

    # get the convex hull

    list_convex_hull = convex_hull(sorted_points)
    # run your test cases

    # print your results to standard output

    # print the convex hull
    print(list_convex_hull)
    # get the area of the convex hull
    area_convex_hull = area_poly(list_convex_hull)
    # print the area of the convex hull
    print(area_convex_hull)

if __name__ == "__main__":
    main()
