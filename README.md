# rumgym

This is the rum-gym module.

## Point
```python
Point(self, x:float=0, y:float=0, z:float=0)
```

This class is a point with x,y,z coordinates.

Variables:
x -- float
y -- float
z -- float

Methods:
__init__(x,y,z) -- Constructor that sets all variables to the given parameters or 0.

## Vector
```python
Vector(self, x:float=0, y:float=0, z:float=0)
```

This class is a child of Point, representing a vector with x,y,z coordinates.

Variables:
x -- float
y -- float
z -- float

Methods:
__init__(x,y,z) -- Constructor that sets all variables to the given parameters or 0.
len() -- Calculates the length of the vector.
scale(s) -- Scales the vecetor with the scalar s.
dot(v1, v2) -- Calculates the dot product of two vectors.
cross(v1, v2) -- Returns the cross product of two vectors.

## Line
```python
Line(self, p:rumgym.Point=<rumgym.Point object at 0x0000019B0B1BC9E8>, d:rumgym.Vector=<rumgym.Vector object at 0x0000019B0B2BADA0>)
```

This class represents a line

Variables:
p -- Point
d -- Vector

Methods:
__init__(p, d) -- Sets the variables to the provided parameters.
len() -- Calculates the length of the line.

## Plane
```python
Plane(self, p:rumgym.Point=<rumgym.Point object at 0x0000019B0B32C358>, d1:rumgym.Vector=<rumgym.Vector object at 0x0000019B0B32C390>, d2:rumgym.Vector=<rumgym.Vector object at 0x0000019B0B32C3C8>)
```

This class represents a plane made from a point and two vectors

Variables:
p -- Point
d1 -- Vector
d2 -- Vector

Methods:
__init__(p, d1, d2) -- Sets the variables to the provided parameters.
normVec() -- Returns the normal vector to the plane.

## Arrow3D
```python
Arrow3D(self, xs, ys, zs, *args, **kwargs)
```

This is an outsourced class, stolen from stackoverflow, with my partner in crime bing.com

## Grapher
```python
Grapher(self)
```

This class draws all the classes from the rumgym library in a plot from matplot lib.

Variables:
fig -- matplotlib.figure()
ax -- plot

Methods:
__init__(obj) -- Turns the given object into a plot and adds it to the combined plot
show() -- Displays the plots made.

