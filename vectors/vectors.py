import math

class Vector(object):
    """ A simple vector toolikt dealing with vectors in the 3-dimensional
        space. """

    def __init__(self, vector):
        """ Argument vector is of type list. """

        self.coordinates = vector  
        self.x = vector[0]
        self.y = vector[1]
        self.z = vector[2]

    def __repr__(self):
        return 'Vector({0}, {1}, {2})'.format(self.x, self.y, self.z)

    def multiply(self, number):
        """ Return a Vector instance as the product of the vector and a real
            number. """

        return Vector([x * number for x in self.coordinates])
    
    def magnitude(self):
        """ Return magnitude of the vector. """

        return (math.sqrt(reduce(lambda x,y: x+y, 
                [x**2 for x in self.coordinates])))

    def add(self, vector):
        """ Return a Vector instance as the vector sum of two vectors. """

        return (Vector([x+vector.coordinates[self.coordinates.index(x)]
                for x in self.coordinates]))

    def substract(self, vector):
        """ Return a Vector instance as the vector difference of two vectors.
        """

        return (Vector([vector.coordinates[self.coordinates.index(x)]-x for x in
                    self.coordinates]))

    def dot(self, vector, theta=None):
        """ Return the dot product of two vectors. If theta is given then the
        dot product is computed as v1*v1 = |v1||v2|cos(theta). Argument theta
        is measured in degrees. """

        if theta is not None:
            return (self.magnitude() * vector.magnitude() *
                    math.degress(math.cos(theta)))
        return (reduce(lambda x,y: x+y,
                [x*vector.coordinates[self.coordinates.index(x)]
                for x in self.coordinates]))

    def cross(self, vector):
        """ Return a Vector instance as the cross product of two vectors """

        return Vector([(self.y * vector.z - self.z * vector.y),
                        (self.z * vector.x - self.x * vector.z),
                        (self.x * vector.y - self.y * vector.x)])

    def angle(self, vector): 
        """ Return the angle between two vectors in degrees. """

        return (math.degrees(math.acos((self.dot(vector) / (self.magnitude() *
            vector.magnitude())))))

    def is_parallel(self, vector):
        """ Return True if vectors are parallel to each other. """

        if self.cross(vector).magnitude() == 0:
            return True
        return False

    def is_perpendicular(self, vector):
        """ Return True if vectors are perpendicular to each other. """

        if self.dot(vector) == 0:
            return True
        return False
