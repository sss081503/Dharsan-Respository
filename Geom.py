import math
class Point (object):
	#constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        #self is a pronoun
        #self stands for the object that gets created when you create the class
        #self is an address in memory of where the object is located

        #get the distance to another point
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
        
	#override an inherited function
        #string representation of a Point
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

        #test for equality of two Points
    def __eq__(self, other):
        tol = 1.0e-6 #tolerance
        #numbers cannot be compared for equality because there is a limit to how precise floating numbers can be represented
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
    #constructor
    def __init__(self, radius = 1, x = 0, y = 0):
        self.radius = radius
        self.center = Point (x, y)

    #compute the circumference
    def circumference (self):
        return 2.0 * math.pi * self.radius

    #compute the area
    def area (self):
        return math.pi * math.pow(radius, 2)

    #determine if a Point p is strictly inside the circle
    def point_inside (self, p):
        return self.center.dist(p) < self.radius

    #determine if a Circle c is strictly inside this circle
    def circle_inside(self, c):
        return (self.center.dist(c.center) + c.radius) < self.radius)

    #determine if a Circle c is strictly outside this circle
    def circle_outside(self, c):
        return (self.center.dist(c.center) - c.radius) > self.radius)

    

def main():
    #create Point objects
    a = Point()
    b = Point(3, 4)
    c = Point(3, 4)

    #print the Point objects
    print(a)
    print(b)
    print(c)

    #print the distance
    print (a.dist(b))
    print (b.dist(a))
main()

