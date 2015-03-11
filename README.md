# Vectors
Vectors is a simple library toolkit dealing with common vector logic in the
3-dimensional space.

Supports commonly used vector math functions including:
  * Addition with another vector or a real number.
  * Multiplication by another vector or a real number.
  * Dot product
  * Cross/scalar product
  * Angle between vectors
  * Check if two vectors are perpendicular, parallel or non-parallel

# Installation

```
pip install vectors
```

# Documentation

##Usage 
We initialize two Vector instances after we import Vector module.

```Python
from vectors import Vector

v1 = Vector(1, 2, 3) #=> Vector(1, 2, 3)
v2 = Vector(2, 4, 6) #=> Vector(2, 4, 6)
```

We can also initialize a Vector instance with a list using the class method
from_list().

```Python
components = [1.2, 2.4, 3.8]

v = Vector.from_list(components) #=> Vector(1.2, 2.4, 3.8)
```

##Addition

We can add a real number to a vector or compute the vector sum of two
vectors as follows.

```Python
v1.add(2) #=> Vector(3.0, 4.0, 5.0)

v1.sum(v2) #=> Vector(3.0, 6.0, 9.0)
```
Both methods return a Vector instance.

##Multiplication

We can multiply a vector by a real number.

```Python
v1.multiply(4) #=> Vector(4.0, 8.0, 12.0)
```
The above returns a Vector instance.

##Dot Product

We can find the dot product of two vectors.

```Python
v1.dot(v2) #=> 28
```
We can also use angle theta on the dot function.

```Python
v1.dot(v2. 180)
```
Dot product returns a real number.

##Cross/Scalar Product

We can find the cross product of two vectors.

```Python
v1.cross(v2) #=> Vector(0, 0, 0)
```
Cross product returns a Vector instance, which is always perpendicular to the
other two vectors.

##Angle Theta

We can also find the angle theta between two vectors.

```Python
v1.angle(v2) #=> 0.0
```
Angle is a measured in degrees.

##Parallel, Perpendicular, Non-Parallel

We can check if two vectors are parallel, perpendicular or non-parallel to each other.

```Python
v1.parallel(v2) #=> True
v1.perpendicular(v2) #=> False
v1.non_parallel(v2) #=> False
```
All of the above return either True or False.









