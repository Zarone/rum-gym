'''
This is the rum-gym module.
'''
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D, proj3d
import numpy as np
class Point():
    '''
    This class is a point with x,y,z coordinates.

    Variables:
    x -- float
    y -- float
    z -- float

    Methods:
    __init__(x,y,z) -- Constructor that sets all variables to the given parameters or 0.
    '''
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        '''
        Constructor that sets all variables to the given parameters or 0.
        '''
        self.x = x
        self.y = y
        self.z = z

class Vector(Point):
    '''
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
    '''
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        '''
        Constructor that sets all variables to the given parameters or 0.
        '''
        super().__init__(x, y, z)
        self.dot = self.__dot

    def len(self) -> float:
        '''
        Returns the length of the vector.
        '''
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)

    def scale(self, s):
        '''
        Scales the vector with the scalar s.
        '''
        self.x *= s
        self.y *= s
        self.z *= s

    def normalize(self):
        '''
        Turns the vector into a unit-vector
        '''
        return self.scale(1.0/self.len())

    def __dot(self, v1):
        '''
        Returns the dot product of the vector
        '''
        return self.x + v1.x + self.y + v1.y + self.z + v1.z

    def __add__(self, v1):
        self.x += v1.x
        self.y += v1.y
        self.z += v1.z

    def __sub__(self, v1):
        self.x -= v1.x
        self.y -= v1.y
        self.z -= v1.z

    @classmethod
    def add(cls, v1, v2):
        '''
        Adds two vectors together
        '''
        x = v1.x + v2.x
        y = v1.y + v2.y
        z = v1.z + v2.z
        return cls(x, y, z)

    @classmethod
    def sub(cls, v1, v2):
        '''
        Subtracts two vectors from eachother
        '''
        x = v1.x - v2.x
        y = v1.y - v2.y
        z = v1.z - v2.z
        return cls(x, y, z)

    @classmethod
    def cross(cls, v1, v2):
        '''
        Returns the cross product of two vectors.
        '''
        x = v1.y *v2.z - v1.z*v2.y
        y = -(v1.z*v2.x - v1.x*v2.z)
        z = v1.x*v2.y - v1.y*v2.x

        return cls(x, y, z)

    @staticmethod
    def dot(v1, v2):
        '''
        Returns the dot product of two vectors.
        '''
        return v1.x + v2.x + v1.y + v2.y + v1.z + v2.z

class Line():
    '''
    This class represents a line

    Variables:
    p -- Point
    d -- Vector

    Methods:
    __init__(p, d) -- Sets the variables to the provided parameters.
    len() -- Calculates the length of the line.
    '''
    def __init__(self, p: Point = Point(), d: Vector = Vector()):
        '''
        Sets the variables to the provided parameters.
        '''
        if isinstance(d, Vector):
            self.p = p
            self.d = d
        elif isinstance(d, Point):
            self.twoPoints(p, d)

        

    def len(self) -> float:
        '''
        Calculates the length of the line.
        '''
        return self.d.len()

    @classmethod
    def twoPoints(cls, p1, p2):
        '''
        Factory method for creating a line from two points
        '''
        v1 = Vector(p1.x - p2.x,
                    p1.y - p2.y,
                    p1.z - p2.z)
        return cls(p1, v1)

class Plane():
    '''
    This class represents a plane made from a point and two vectors

    Variables:
    p -- Point
    d1 -- Vector
    d2 -- Vector

    Methods:
    __init__(p, d1, d2) -- Sets the variables to the provided parameters.
    normVec() -- Returns the normal vector to the plane.
    angle() -- Returns the angle between the plane and a vector.
    '''
    def __init__(self, p: Point = Point(), d1: Vector = Vector(), d2: Vector = Vector()):
        '''
        Sets the variables to the provided parameters.
        '''
        if isinstance(p, Point) and isinstance(d1, Vector) and isinstance(d2, Vector):
            self.p = p
            self.d1 = d1
            self.d2 = d2
        elif isinstance(p, Point) and isinstance(d1, Point) and isinstance(d2, Point):
            self.threePoints(p, d1, d2)
        elif isinstance(p, Vector) and isinstance(d1, Point) and isinstance(d2, Point):
            self.vecTwoPoints(p, d1, d2)
        

    def normVec(self) -> Vector:
        '''
        Returns the normal vector to the plane.
        '''
        nv = Vector.cross(self.d1, self.d2)
        nv.normalize()

        return nv

    def angle(self, v: Vector) -> float:
        '''
        Returns the angle between the plane and a vector.
        '''
        pass
    
    def getZCoord(self, x, y):
        '''
        Returns a z-coord in the plane, from given x and y
        '''
        n = self.normVec()
        z = (-n.x*(x - self.p.x) - n.y*(y - self.p.y) + n.z*self.p.z)/n.z
        return z

    @classmethod
    def vecTwoPoints(cls, nv, p1, p2):
        '''
        Factory method for creating a plane from a unit vector and two points
        '''
        p = Point(nv.x, nv.y, nv.z)
        return cls(p, p1, p2)

    @classmethod
    def threePoints(cls, p1, p2, p3):
        '''
        Factory method for creating a plane from three points
        '''
        v1 = Vector(p2)
        v2 = Vector(p3)
        return cls(p1, v1, v2)

class Arrow3D(FancyArrowPatch):
    '''
    '''
    def __init__(self, xs, ys, zs, *args, **kwargs):
        '''
        '''
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        '''
        '''
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

class Grapher():
    '''
    Fek me
    '''
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.gca(projection='3d')

    def add(self, obj):
        '''
        im not working
        '''
        if isinstance(obj, Vector):
            a = Arrow3D([0, obj.x], [0, obj.y], [0, obj.z], mutation_scale=20, arrowstyle="-|>", color="k")
            self.ax.add_artist(a)
            self.ax.scatter([0, obj.x], [0, obj.y], [0, obj.z], alpha=0)
        elif isinstance(obj, Point):
            self.ax.scatter(obj.x, obj.y, obj.z)
        elif isinstance(obj, Line):
            self.ax.plot([obj.p.x, obj.d.x], [obj.p.y, obj.d.y], [obj.p.z, obj.d.z])
        elif isinstance(obj, Plane):
            x = np.arange(-10, 10, 0.25)
            y = np.arange(-10, 10, 0.25)
            x, y = np.meshgrid(x, y)
            zs = np.array([obj.getZCoord(x, y) for x, y in zip(np.ravel(x), np.ravel(y))])
            z = zs.reshape(x.shape)

            surf = self.ax.plot_surface(x, y, z, linewidth=0, antialiased=False, alpha=0.3)
        else:
            print("You did not give me anything to work with!")
        plt.autoscale(enable=True, axis='both', tight=False)

    def show(self):
        '''
        Shows the plots made.
        '''
        plt.show()
