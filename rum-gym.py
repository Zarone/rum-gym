
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
        return self.scale(1.0/self.len)
         
    def __dot(self, v1):
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
        x = v1.x + v2.x
        y = v1.y + v2.y
        z = v1.z + v2.z
        return cls(x, y, z)
    
    @classmethod
    def sub(cls, v1, v2):
        x = v1.x - v2.x
        y = v1.y - v2.y
        z = v1.z - v2.z
        return cls(x, y, z)

    @classmethod
    def dot(cls, v1, v2):
        '''
        Returns the dot product of two vectors.
        '''
        return v1.x + v2.x + v1.y + v2.y + v1.z + v2.z

    @classmethod
    def cross(cls, v1, v2):
        '''
        Returns the cross product of two vectors.
        '''
        x = v1.y *v2.z - v1.z*v2.y
        y = -(v1.z*v2.x - v1.x*v2.z)
        z = v1.x*v2.y - v1.y*v2.x
        
        return cls(x,y,z)

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
        if isinstance(d, Point):
            self.twoPoints(p, d)

        self.p = p
        self.d = d
    
    def len(self) -> float:
        '''
        Calculates the length of the line.
        '''
        return self.d.len()
    
    @classmethod
    def twoPoints(cls, p1, p2):
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
        if isinstance(p, Vector) and isinstance(d1, Point) and isinstance(d2, Point):
            self.vecTwoPoints(p, d1, d2)
        
        elif isinstance(p, Point) and isinstance(d1, Point) and isinstance(d2, Point):
            self.threePoints(p, d1, d2)

        self.p = p
        self.d1 = d1
        self.d2 = d2
    
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
    
    @classmethod
    def vecTwoPoints(cls, nv, p1, p2):
        p = Point(nv.x, nv.y, nv.z)
        return cls(p, p1, p2)
    
    @classmethod
    def threePoints(cls, p1, p2, p3):
        v1 = Vector(p2)
        v2 = Vector(p3)
        return cls(p1, v1, v2)



