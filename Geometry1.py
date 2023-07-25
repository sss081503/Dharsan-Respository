
#  File: Geometry.py

#  Description:

#  Student Name: Dharsan Selvakumar

#  Student UT EID: ss96967

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import math


class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      self.x = x
      self.y = y
      self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
      return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)
    
  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
      tol = 1.0e-6 #tolerance
      return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))






    

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
      self.radius = radius
      self.center = Point(x, y, z)

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
      return "Center: " + self.center + ", Radius: " + self.radius

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
      return 4.0 * math.pi * self.radius * self.radius

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
      return (4.0 * math.pi * math.pow(self.radius, 3))/3.0

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
      return self.center.distance(p) < self.radius
      

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
      return (self.center.distance(other.center) + other.radius) < self.radius
      

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      # return (self.center.distance(a_cube.center) + a_cube.diagonal < self.radius)
      center_of_cube = a_cube.center
      point1 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point2 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
      point3 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point4 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
      point5 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point6 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
      point7 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point8 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
                     
      if ((self.is_inside_point(point1) == True) and (self.is_inside_point(point2) == True) and (self.is_inside_point(point3) == True) and (self.is_inside_point(point4) == True)
      and (self.is_inside_point(point5) == True) and (self.is_inside_point(point6) == True) and (self.is_inside_point(point7) == True) and (self.is_inside_point(point8) == True)):
          return True
      else:
          return False
      

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
      center_cyl = a_cyl.center
      point1 = Point(center_cyl.x + a_cyl.radius, center_cyl.y + a_cyl.radius, center_cyl.z + (a_cyl.height)/2)
      point2 = Point(center_cyl.x + a_cyl.radius, center_cyl.y + a_cyl.radius, center_cyl.z - (a_cyl.height)/2)
      point3 = Point(center_cyl.x + a_cyl.radius, center_cyl.y - a_cyl.radius, center_cyl.z + (a_cyl.height)/2)
      point4 = Point(center_cyl.x + a_cyl.radius, center_cyl.y - a_cyl.radius, center_cyl.z - (a_cyl.height)/2)
      point5 = Point(center_cyl.x - a_cyl.radius, center_cyl.y + a_cyl.radius, center_cyl.z + (a_cyl.height)/2)
      point6 = Point(center_cyl.x - a_cyl.radius, center_cyl.y + a_cyl.radius, center_cyl.z - (a_cyl.height)/2)
      point7 = Point(center_cyl.x - a_cyl.radius, center_cyl.y - a_cyl.radius, center_cyl.z + (a_cyl.height)/2)
      point8 = Point(center_cyl.x - a_cyl.radius, center_cyl.y - a_cyl.radius, center_cyl.z - (a_cyl.height)/2)

      if ((self.is_inside_point(point1) == True) and (self.is_inside_point(point2) == True) and (self.is_inside_point(point3) == True) and (self.is_inside_point(point4) == True)
      and (self.is_inside_point(point5) == True) and (self.is_inside_point(point6) == True) and (self.is_inside_point(point7) == True) and (self.is_inside_point(point8) == True)):
          return True
      else:
          return False


  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean


  # helper functions
  #determine if a Sphere c is strictly inside this sphere
  def sphere_inside(self, c):
        return (self.center.dist(c.center) + c.radius) < self.radius

   #determine if a Sphere c is strictly outside this sphere
  def sphere_outside(self, c):
        return (self.center.dist(c.center) - c.radius) > self.radius

  
  def does_intersect_sphere (self, other):
      if (self.sphere_inside(other) == False) and (self.sphere_outside(other) == False):
          return True
      else:
          return False
      

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean

  # helper function
  def is_outside_cube (self, a_cube):
      # return (self.center.distance(a_cube.center) + a_cube.diagonal < self.radius)
      center_of_cube = a_cube.center
      point1 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point2 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
      point3 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point4 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
      point5 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point6 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
      point7 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point8 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
                     
      if ((self.is_inside_point(point1) == False) and (self.is_inside_point(point2) == False) and (self.is_inside_point(point3) == False) and (self.is_inside_point(point4) == False)
      and (self.is_inside_point(point5) == False) and (self.is_inside_point(point6) == False) and (self.is_inside_point(point7) == False) and (self.is_inside_point(point8) == False)):
          return True
      else:
          return False
  
  def does_intersect_cube (self, a_cube):
      if (self.is_inside_cube(a_cube) == False) and (self.is_outside_cube(a_cube) == False):
          return True
      else:
          return False
      

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
      cube_side = (2/(math.sqrt(3))) * self.radius
      return Cube(self.x, self.y, self.z, cube_side)





class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
      self.x = x
      self.y = y
      self.z = z
      self.side = 1
      self.center = Point(x, y, z)
      
  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
      return "(" + self.x + ", " + self.y + ", " + self.z + "), Side: " + self.side

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
      return 6.0 * self.side * self.side

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
  
      return float(math.pow(self.side, 3)


  # creating new function to calculate diagonal length from center to any vertex of cube
  # helper function
  #def diagonal (self):
      #return (math.sqrt(3)/2) * self.side
      

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):

      x_distance = abs(float((self.center.x - p.x))
      y_distance = abs(float(self.center.y - p.y))
      z_distance = abs(float(self.center.z - p.z))

      return (x_distance < self.side/2.0) and (y_distance < self.side/2.0) and (z_distance < self.side/2.0):
         
      

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      side_length = a_sphere.radius * 2
      new_cube = Cube(a_sphere.center.x, a_sphere.center.y, a_sphere.center.z, side_length)
      if self.is_inside_cube(new_cube) == True:
          return True
      else:
          return False

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
      point1 = Point(other.center.x + (other.side/2), other.center.y + (other.side/2), other.center.z + (other.side/2))
      point2 = Point(other.center.x + (other.side/2), other.center.y + (other.side/2), other.center.z - (other.side/2))
      point3 = Point(other.center.x + (other.side/2), other.center.y - (other.side/2), other.center.z + (other.side/2))
      point4 = Point(other.center.x + (other.side/2), other.center.y - (other.side/2), other.center.z - (other.side/2))
      point5 = Point(other.center.x - (other.side/2), other.center.y + (other.side/2), other.center.z + (other.side/2))
      point6 = Point(other.center.x - (other.side/2), other.center.y + (other.side/2), other.center.z - (other.side/2))
      point7 = Point(other.center.x - (other.side/2), other.center.y - (other.side/2), other.center.z + (other.side/2))
      point8 = Point(other.center.x - (other.side/2), other.center.y - (other.side/2), other.center.z - (other.side/2))

      if ((self.is_inside_point(point1) == True) and (self.is_inside_point(point2) == True) and (self.is_inside_point(point3) == True) and (self.is_inside_point(point4) == True)
      and (self.is_inside_point(point5) == True) and (self.is_inside_point(point6) == True) and (self.is_inside_point(point7) == True) and (self.is_inside_point(point8) == True)):
          return True
      else:
          return False

      

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
      center_cyl = a_cyl.center
      point1 = Point(center_cyl.x + a_cyl.radius, center_cyl.y + a_cyl.radius, center_cyl.z + (a_cyl.height)/2)
      point2 = Point(center_cyl.x + a_cyl.radius, center_cyl.y + a_cyl.radius, center_cyl.z - (a_cyl.height)/2)
      point3 = Point(center_cyl.x + a_cyl.radius, center_cyl.y - a_cyl.radius, center_cyl.z + (a_cyl.height)/2)
      point4 = Point(center_cyl.x + a_cyl.radius, center_cyl.y - a_cyl.radius, center_cyl.z - (a_cyl.height)/2)
      point5 = Point(center_cyl.x - a_cyl.radius, center_cyl.y + a_cyl.radius, center_cyl.z + (a_cyl.height)/2)
      point6 = Point(center_cyl.x - a_cyl.radius, center_cyl.y + a_cyl.radius, center_cyl.z - (a_cyl.height)/2)
      point7 = Point(center_cyl.x - a_cyl.radius, center_cyl.y - a_cyl.radius, center_cyl.z + (a_cyl.height)/2)
      point8 = Point(center_cyl.x - a_cyl.radius, center_cyl.y - a_cyl.radius, center_cyl.z - (a_cyl.height)/2)

      if ((self.is_inside_point(point1) == True) and (self.is_inside_point(point2) == True) and (self.is_inside_point(point3) == True) and (self.is_inside_point(point4) == True)
      and (self.is_inside_point(point5) == True) and (self.is_inside_point(point6) == True) and (self.is_inside_point(point7) == True) and (self.is_inside_point(point8) == True)):
          return True
      else:
          return False
      

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean

  # helper function
  def is_outside_cube (self, other):
      point1 = Point(other.center.x + (other.side/2), other.center.y + (other.side/2), other.center.z + (other.side/2))
      point2 = Point(other.center.x + (other.side/2), other.center.y + (other.side/2), other.center.z - (other.side/2))
      point3 = Point(other.center.x + (other.side/2), other.center.y - (other.side/2), other.center.z + (other.side/2))
      point4 = Point(other.center.x + (other.side/2), other.center.y - (other.side/2), other.center.z - (other.side/2))
      point5 = Point(other.center.x - (other.side/2), other.center.y + (other.side/2), other.center.z + (other.side/2))
      point6 = Point(other.center.x - (other.side/2), other.center.y + (other.side/2), other.center.z - (other.side/2))
      point7 = Point(other.center.x - (other.side/2), other.center.y - (other.side/2), other.center.z + (other.side/2))
      point8 = Point(other.center.x - (other.side/2), other.center.y - (other.side/2), other.center.z - (other.side/2))

      if ((self.is_inside_point(point1) == False) and (self.is_inside_point(point2) == False) and (self.is_inside_point(point3) == False) and (self.is_inside_point(point4) == False)
      and (self.is_inside_point(point5) == False) and (self.is_inside_point(point6) == False) and (self.is_inside_point(point7) == False) and (self.is_inside_point(point8) == False)):
          return True
      else:
          return False

  
  def does_intersect_cube (self, other):
      if ((self.is_inside_cube(other) == False) and (self.is_outside_cube(other) == False)):
          return True
      else:
          return False

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    if (self.side > other.side):
        
      big = self
      small = other
      
    else:
        
      big = other
      small = self

    small_len = small.side/2
    big_len = big.side/2

    if (self.does_intersect_cube(other)):
      minx = min(small.center.x + small_len, big.center.x + big_len) 
      maxx = max(small.center.x - small_len, big.center.x - big_len)
      miny = min(small.center.y + small_len, big.center.y + big_len)
      maxy = max(small.center.y - small_len, big.center.y - big_len)
      minz = min(small.center.z + small_len, big.center.z + big_len)
      maxz = max(small.center.z - small_len, big.center.z - big_len)

      distx = minx - maxx
      disty = miny - maxy
      distz = minz - maxz
      
      return (distx * disty * distz)
    else:
      return 0
          

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
      return Sphere(self.x, self.y, self.z, self.side/2)







      

class Cylinder(object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      self.x = x
      self.y = y
      self.z = z
      self.center = Point(x, y, z)
      self.radius = radius
      self.height = height

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
      return "(" + self.x + ", " + self.y + ", " + self.z + "), Radius: " + self.radius + ", Height: " + self.height

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
      surface_area = (2.0 * math.pi * self.radius * self.height) + (2.0 * math.pi * self.radius * self.radius)
      return surface_area

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
      return math.pi * self.radius * self.radius * self.height

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    if (abs(self.center.z-p.z)< self.height/2) and (math.hypot((self.center.x-p.x),(self.center.y-p.y)) < self.radius):
        return True
    else:
        return False

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):

      center_distance = math.hypot(self.center.x-a_sphere.center.x, self.center.y-a_sphere.center.y)
      valid1 = center_distance + a_sphere.radius < self.radius
      if valid1 and (a_sphere.center.z < self.center.z + (self.height/2) - a_sphere.radius) and (a_sphere.center.z > self.center.z - self.height + a_sphere.radius):
          return True
      else:
          return False

      

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      center_of_cube = a_cube.center
      point1 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point2 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
      point3 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point4 = Point(center_of_cube.x + (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
      point5 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point6 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y + (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
      point7 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z + (a_cube.side/2))
      point8 = Point(center_of_cube.x - (a_cube.side/2), center_of_cube.y - (a_cube.side/2), center_of_cube.z - (a_cube.side/2))
                     
      if ((self.is_inside_point(point1) == True) and (self.is_inside_point(point2) == True) and (self.is_inside_point(point3) == True) and (self.is_inside_point(point4) == True)
      and (self.is_inside_point(point5) == True) and (self.is_inside_point(point6) == True) and (self.is_inside_point(point7) == True) and (self.is_inside_point(point8) == True)):
          return True
      else:
          return False

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
      center_cyl = other.center
      point1 = Point(center_cyl.x + other.radius, center_cyl.y + other.radius, center_cyl.z + (other.height)/2)
      point2 = Point(center_cyl.x + other.radius, center_cyl.y + other.radius, center_cyl.z - (other.height)/2)
      point3 = Point(center_cyl.x + other.radius, center_cyl.y - other.radius, center_cyl.z + (other.height)/2)
      point4 = Point(center_cyl.x + other.radius, center_cyl.y - other.radius, center_cyl.z - (other.height)/2)
      point5 = Point(center_cyl.x - other.radius, center_cyl.y + other.radius, center_cyl.z + (other.height)/2)
      point6 = Point(center_cyl.x - other.radius, center_cyl.y + other.radius, center_cyl.z - (other.height)/2)
      point7 = Point(center_cyl.x - other.radius, center_cyl.y - other.radius, center_cyl.z + (other.height)/2)
      point8 = Point(center_cyl.x - other.radius, center_cyl.y - other.radius, center_cyl.z - (other.height)/2)

      if ((self.is_inside_point(point1) == True) and (self.is_inside_point(point2) == True) and (self.is_inside_point(point3) == True) and (self.is_inside_point(point4) == True)
      and (self.is_inside_point(point5) == True) and (self.is_inside_point(point6) == True) and (self.is_inside_point(point7) == True) and (self.is_inside_point(point8) == True)):
          return True
      else:
          return False

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean

  # helper function
  def is_outside_cylinder (self, other):
      center_cyl = other.center
      point1 = Point(center_cyl.x + other.radius, center_cyl.y + other.radius, center_cyl.z + (other.height)/2)
      point2 = Point(center_cyl.x + other.radius, center_cyl.y + other.radius, center_cyl.z - (other.height)/2)
      point3 = Point(center_cyl.x + other.radius, center_cyl.y - other.radius, center_cyl.z + (other.height)/2)
      point4 = Point(center_cyl.x + other.radius, center_cyl.y - other.radius, center_cyl.z - (other.height)/2)
      point5 = Point(center_cyl.x - other.radius, center_cyl.y + other.radius, center_cyl.z + (other.height)/2)
      point6 = Point(center_cyl.x - other.radius, center_cyl.y + other.radius, center_cyl.z - (other.height)/2)
      point7 = Point(center_cyl.x - other.radius, center_cyl.y - other.radius, center_cyl.z + (other.height)/2)
      point8 = Point(center_cyl.x - other.radius, center_cyl.y - other.radius, center_cyl.z - (other.height)/2)

      if ((self.is_inside_point(point1) == False) and (self.is_inside_point(point2) == False) and (self.is_inside_point(point3) == False) and (self.is_inside_point(point4) == False)
      and (self.is_inside_point(point5) == False) and (self.is_inside_point(point6) == False) and (self.is_inside_point(point7) == False) and (self.is_inside_point(point8) == False)):
          return True
      else:
          return False
        
  def does_intersect_cylinder (self, other):
      if (self.is_inside_cylinder(other) == False) and (self.is_outside_cylinder(other) == False):
          return True
      else:
          return False

def main():


    
  # read data from standard input

  # read the coordinates of the first Point p
  p = input()

  # create a Point object
  p = p.split(" ")
  point_p = Point(float(p[0]),float(p[1]),float(p[2]))

  # read the coordinates of the second Point q
  q = input()

  # create a Point object 
  q = q.split(" ")
  point_q = Point(float(q[0]),float(q[1]),float(q[2]))

  # read the coordinates of the center and radius of sphereA
  a = input()

  # create a Sphere object
  a = a.split(" ")
  sphereA = Sphere(float(a[0]),float(a[1]),float(a[2]),float(a[3]))
  

  # read the coordinates of the center and radius of sphereB
  b = input()

  # create a Sphere object
  b = b.split(" ")
  sphereB = Sphere(float(b[0]),float(b[1]),float(b[2]),float(b[3]))

  # read the coordinates of the center and side of cubeA
  cube_a = input()

  # create a Cube object
  cube_a = cube_a.split(" ")
  cubeA = Cube(float(cube_a[0]),float(cube_a[1]),float(cube_a[2]),float(cube_a[3]))

  # read the coordinates of the center and side of cubeB
  cube_b = input()

  # create a Cube object
  cube_b = cube_b.split(" ")
  cubeB = Cube(float(cube_b[0]),float(cube_b[1]),float(cube_b[2]),float(cube_b[3]))

  # read the coordinates of the center, radius and height of cylA
  cyl_a = input()

  # create a Cylinder object
  cyl_a = cyl_a.split(" ")
  cylA = Cylinder((float(cyl_a[0]),float(cyl_a[1]),float(cyl_a[2]),float(cyl_a[3]),float(cyl_a[4])) 

  # read the coordinates of the center, radius and height of cylB
  cyl_b = input()

  # create a Cylinder object
  cyl_b = cyl_b.split(" ")
  cylB = Cylinder((float(cyl_b[0]),float(cyl_b[1]),float(cyl_b[2]),float(cyl_b[3]),float(cyl_b[4]))

  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
  if point_p.distance(Point(0,0,0) > point_q.distance(Point(0,0,0):
    print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
  else:
    print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

  # print if Point p is inside sphereA
  if sphereA.is_inside_point(point_p):
    print("Point p is inside sphereA")
  else:
    print("Point p is not inside sphereA")

  # print if sphereB is inside sphereA
  if sphereA.is_inside_sphere(sphereB):
    print("sphereB is inside sphereA")
  else:
    print("sphereB is not inside sphereA")

  # print if cubeA is inside sphereA
  if sphereA.is_inside_cube(cubeA):
    print("cubeA is inside sphereA")
  else:
    print("cubeA is not inside sphereA")

  # print if cylA is inside sphereA
  if sphereA.is_inside_cyl(cylA):
    print("cylA is inside sphere A")
  else:
    print("cylA is not inside sphere A")

  # print if sphereA intersects with sphereB
  if (sphereA.does_intersect_sphere(sphereB)):
    print('sphereA does intersect sphereB')
  else:
    print('sphereA does not intersect sphereB')

  # print if cubeB intersects with sphereB
  if sphereB.does_intersect_cube(cubeB):
    print("cubeB does intersect sphereB")
  else:
    print("cubeB does not intersect sphereB")

  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  if sphereA.circumscribe_cube.volume > cylA.volume:
    print("Volume of the largest Cube that is cirucmscribed by sphereA is greater than the volume of cylA")
  else:
    print("Volume of the largest Cube that is cirucmscribed by sphereA is not greater than the volume of cylA")

  # print if Point p is inside cubeA
  if cubeA.is_inside_point(point_p):
    print("Point p is inside cubeA")
  else:
    print("Point p is not inside cubeA")

  # print if sphereA is inside cubeA
  if cubeA.is_inside_sphere(sphereA):
    print("sphereA is inside cubeA")
  else:
    print("sphereA is not inside cubeA")

  # print if cubeB is inside cubeA
  if cubeA.is_inside_cube(cubeB):
    print("cubeB is inside cubeA")
  else:
    print("cubeB is not inside cubeA")

  # print if cylA is inside cubeA
  if cubeA.is_inside_cylinder(cylA):
    print("cylA is inside cubeA")
  else:
    print("cylA is not inside cubeA")

  # print if cubeA intersects with cubeB
  if cubeA.does_intersect_cube(cubeB):
    print("cubeA does intersect cubeB")
  else:
    print("cubeA does not intersect cubeB")

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if cubeA.intersection_volume(cubeB) > sphereA.volume:
    print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
  else:
    print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  if cubeA.inscribe_sphere.surface_area > cylA.surface_area:
    print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
  else:
    print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")

  # print if Point p is inside cylA
  if cylA.is_inside_point(point_p):
    print("Point p is inside cylA")
  else:
    print("Point p is not inside cylA")

  # print if sphereA is inside cylA
  if cylA.is_inside_sphere(sphereA):
    print("sphereA is inside cylA")
  else:
    print("sphereA is not inside cylA")

  # print if cubeA is inside cylA
  if cylA.is_inside_cube(cubeA):
    print("cubeA is inside cylA")
  else:
    print("cubeA is not inside cylA")

  # print if cylB is inside cylA
  if cylA.is_inside_cylinder(cylB):
    print("cylB is inside cylA")
  else:
    print("cylB is not inside cylA")

  # print if cylB intersects with cylA
  if cylA.does_intersect_cylinder(cylB):
    print("cylB does intersect cylA")
  else:
    print("cylB does not intersect cylA")

if __name__ == "__main__":
  main()

