from __future__ import division
import math
from functools import reduce

class Point(object):
    """ Point class: Reprepsents a point in the x, y, z space. """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return '{0}({1}, {2}, {3})'.format(self.__class__.__name__, self.x,
                                           self.y, self.z)

    def substract(self, point):
        """ Return a Point instance as the displacement of two points. """

        return Point(point.x - self.x, point.y - self.y, point.z - self.z)

    @classmethod
    def from_list(cls, l):
        """ Return a Point instance from a given list """

        x, y, z = map(float, l)
        return cls(x, y, z)


class Vector(Point):
    """ Vector class: Represents a vector in the x, y, z space. """

    def __init__(self, x, y, z):
        self.vector = [x, y, z]
        super(Vector, self).__init__(x, y, z)

    def add(self, number):
        """ Return a Vector instance as the product of the vector and a real
            number. """

        return self.from_list([x+number for x in self.vector])

    def multiply(self, number):
        """ Return a Vector instance as the product of the vector and a real
            number. """

        return self.from_list([x*number for x in self.vector])

    def magnitude(self):
        """ Return magnitude of the vector. """

        return (math.sqrt(reduce(lambda x, y: x+y,
                [x**2 for x in self.vector])))

    def sum(self, vector):
        """ Return a Vector instance as the vector sum of two vectors. """

        return (self.from_list([x+vector.vector[i]
                for i,x in enumerate(self.vector)]))

    def substract(self, vector):
        """ Return a Vector instance as the vector difference of two vectors.
        """

        return (self.from_list([vector.vector[i]-x for i,x in
                                enumerate(self.vector)]))

    def dot(self, vector, theta=None):
        """ Return the dot product of two vectors. If theta is given then the
        dot product is computed as v1*v1 = |v1||v2|cos(theta). Argument theta
        is measured in degrees. """

        if theta is not None:
            return (self.magnitude() * vector.magnitude() *
                    math.degrees(math.cos(theta)))
        return (reduce(lambda x, y: x+y,
                [x*vector.vector[i]
                 for i,x in enumerate(self.vector)]))

    def cross(self, vector):
        """ Return a Vector instance as the cross product of two vectors """

        return Vector((self.y * vector.z - self.z * vector.y),
                      (self.z * vector.x - self.x * vector.z),
                      (self.x * vector.y - self.y * vector.x))

    def angle(self, vector):
        """ Return the angle between two vectors in degrees. """

        return (math.degrees(math.acos((self.dot(vector) / (self.magnitude() *
                vector.magnitude())))))

    def parallel(self, vector):
        """ Return True if vectors are parallel to each other. """

        if self.cross(vector).magnitude() == 0:
            return True
        return False

    def perpendicular(self, vector):
        """ Return True if vectors are perpendicular to each other. """

        if self.dot(vector) == 0:
            return True
        return False

    def non_parallel(self, vector):
        """ Return True if vectors are non-parallel. Non-parallel vectors are
            vectors which are neither parallel nor perpendicular to each other.
        """

        if (self.is_parallel(vector) is not True and
                self.is_perpendicular(vector) is not True):
            return True
        return False
    
    def rotate(self,angle,axis=(0,0,1)):
        """Returns the rotated vector. Assumes angle is in radians"""
        if(type(axis[0])!=int or type(axis[1])!=int or type(axis[2])!=int):
            raise ValueError
            
        x = self.x
        y = self.y
        z = self.z
        
        '''Z axis rotation'''
        if(axis[2]):
            x = x*math.cos(angle) - y*math.sin(angle)
            y = x*math.sin(angle) + y*math.cos(angle)
            #z  = z
            
        '''Y axis rotation'''
        if(axis[1]):
            x = x*math.cos(angle) + z*math.sin(angle)
            #y = y
            z = -x*math.sin(angle) + z*math.cos(angle)
            
        '''X axis rotation'''
        if(axis[0]):
            #x=x
            y = y*math.cos(angle) - z*math.sin(angle)
            z = y*math.sin(angle) + z*math.cos(angle)
            
        return Vector(x,y,z)

    @classmethod
    def from_points(cls, point1, point2):
        """ Return a Vector instance from two given points. """

        if isinstance(point1, Point) and isinstance(point2, Point):
            displacement = point1.substract(point2)
            return cls(displacement.x, displacement.y, displacement.z)
        raise TypeError
