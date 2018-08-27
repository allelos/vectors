from __future__ import division
import math
from numbers import Real
from functools import reduce


class Point(object):
    """Point class: Reprepsents a point in the x, y, z space."""
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return '{0}({1}, {2}, {3})'.format(self.__class__.__name__, self.x, self.y, self.z)

    def __sub__(self, point):
        """Return a Point instance as the displacement of two points."""
        if type(point) is Point:
            return self.substract(point)
        else:
            raise TypeError

    def __add__(self, point):
        if isinstance(point, Point):
            if self.z and point.z:
                return Point(point.x + self.x, point.y + self.y, point.z + self.z)
            elif self.z:
                return Point(point.x + self.x, point.y + self.y, self.z)
            elif point.z:
                return Point(point.x + self.x, point.y + self.y, point.z)
            else:
                return Point(point.x + self.x, point.y + self.y)
        else:
            raise TypeError

    def substract(self, point):
        """Return a Point instance as the displacement of two points."""
        if isinstance(point, Point):
                return Point(point.x - self.x, point.y - self.y, point.z - self.z)
        else:
            raise TypeError

    @classmethod
    def from_list(cls, l):
        """Return a Point instance from a given list"""
        if len(l) == 3:
                x, y, z = map(float, l)
                return cls(x, y, z)
        elif len(l) == 2:
            x, y = map(float, l)
            return cls(x, y)
        else:
            raise AttributeError


class Vector(Point):
    """Vector class: Representing a vector in 3D space.

    Can accept formats of:
    Cartesian coordinates in the x, y, z space.(Regular initialization)
    Spherical coordinates in the r, theta, phi space.(Spherical class method)
    Cylindrical coordinates in the r, theta, z space.(Cylindrical class method)
    """

    def __init__(self, x, y, z):
        '''Vectors are created in rectangular coordniates
        to create a vector in spherical or cylindrical
        see the class methods'''
        super(Vector, self).__init__(x, y, z)

    def __add__(self, anotherVector):
        """Add two vectors together"""
        if(type(anotherVector) == type(self)):
            return Vector(self.x + anotherVector.x, self.y + anotherVector.y, self.z + anotherVector.z)
        elif isinstance(anotherVector, Real):
            return self.add(anotherVector)
        else:
            raise TypeError

    def __sub__(self, anotherVector):
        """Subtract two vectors"""
        if(type(anotherVector) == type(self)):
            return Vector(self.x - anotherVector.x, self.y - anotherVector.y, self.z - anotherVector.z)
        elif isinstance(anotherVector, Real):
            return Vector(self.x - anotherVector, self.y - anotherVector, self.z - anotherVector)
        else:
            raise TypeError

    def __mul__(self, anotherVector):
        """Return a Vector instance as the cross product of two vectors"""
        return self.cross(anotherVector)

    def __str__(self):
        return "{0},{1},{2}".format(self.x, self.y, self.z)

    def add(self, number):
        """Return a Vector instance as the product of the vector and a real number."""
        return self.from_list([x + number for x in self.vector])

    def multiply(self, number):
        """Return a Vector instance as the product of the vector and a real number."""
        return self.from_list([x * number for x in self.vector])

    def magnitude(self):
        """Return magnitude of the vector."""
        return (math.sqrt(reduce(lambda x, y: x + y, [x ** 2 for x in self.vector])))

    def sum(self, vector):
        """Return a Vector instance as the vector sum of two vectors."""
        return (self.from_list([x + vector.vector[i] for i, x in enumerate(self.vector)]))

    def subtract(self, vector):
        """Return a Vector instance as the vector difference of two vectors."""
        return self.__sub__(vector)

    def dot(self, vector, theta=None):
        """Return the dot product of two vectors. If theta is given then the
        dot product is computed as v1*v1 = |v1||v2|cos(theta). Argument theta
        is measured in degrees."""
        if theta is not None:
            return (self.magnitude() * vector.magnitude() *
                    math.degrees(math.cos(theta)))
        return (reduce(lambda x, y: x + y,
                [x * vector.vector[i] for i, x in enumerate(self.vector)]))

    def cross(self, vector):
        """Return a Vector instance as the cross product of two vectors"""
        return Vector((self.y * vector.z - self.z * vector.y),
                      (self.z * vector.x - self.x * vector.z),
                      (self.x * vector.y - self.y * vector.x))

    def unit(self):
        """Return a Vector instance of the unit vector"""
        return Vector(
            (self.x / self.magnitude()),
            (self.y / self.magnitude()),
            (self.z / self.magnitude())
        )

    def angle(self, vector):
        """Return the angle between two vectors in degrees."""
        return (math.degrees(math.acos((self.dot(vector) / (self.magnitude() * vector.magnitude())))))

    def parallel(self, vector):
        """Return True if vectors are parallel to each other."""
        if self.cross(vector).magnitude() == 0:
            return True
        return False

    def perpendicular(self, vector):
        """Return True if vectors are perpendicular to each other."""
        if self.dot(vector) == 0:
            return True
        return False

    def non_parallel(self, vector):
        """Return True if vectors are non-parallel. Non-parallel vectors are
            vectors which are neither parallel nor perpendicular to each other."""
        if (self.is_parallel(vector) is not True and
                self.is_perpendicular(vector) is not True):
            return True
        return False

    def rotate(self, angle, axis=(0, 0, 1)):
        """Returns the rotated vector. Assumes angle is in radians"""
        if(type(axis[0]) != int or type(axis[1]) != int or type(axis[2]) != int):
            raise ValueError
        x = self.x
        y = self.y
        z = self.z
        # Z axis rotation
        if(axis[2]):
            x = x * math.cos(angle) - y * math.sin(angle)
            y = x * math.sin(angle) + y * math.cos(angle)

        # Y axis rotation
        if(axis[1]):
            x = x * math.cos(angle) + z * math.sin(angle)
            z = -x * math.sin(angle) + z * math.cos(angle)

        # X axis rotation
        if(axis[0]):
            # x=x
            y = y * math.cos(angle) - z * math.sin(angle)
            z = y * math.sin(angle) + z * math.cos(angle)

        return Vector(x, y, z)

    def to_points(self):
        ''' Returns an array of [x,y,z] of the end points'''
        return [self.x, self.y, self.z]

    @classmethod
    def from_points(cls, point1, point2):
        """Return a Vector instance from two given points."""
        if isinstance(point1, Point) and isinstance(point2, Point):
            displacement = point1.substract(point2)
            return cls(displacement.x, displacement.y, displacement.z)
        raise TypeError

    @classmethod
    def spherical(cls, mag, theta, phi=0):
        '''Returns a Vector instance from spherical coordinates'''
        return cls(mag * math.sin(phi) * math.cos(theta), mag * math.sin(phi) * math.sin(theta), mag * math.cos(phi))

    @classmethod
    def cylindrical(cls, mag, theta, z=0):
        '''Returns a Vector instance from cylindircal coordinates'''
        return cls(mag * math.cos(theta), mag * math.sin(theta), z)
