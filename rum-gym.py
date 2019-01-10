
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
    '''
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        '''
        Constructor that sets all variables to the given parameters or 0.
        '''
        super().__init__(x, y, z)
        
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

    @staticmethod
    def dot(v1: Vector, v2: Vector) -> Vector:
        '''
        Returns the dot product of two vectors.
        '''
        return Vector()

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
        self.p = p
        self.d = d
    
    def len(self) -> float:
        '''
        Calculates the length of the line.
        '''
        return self.d.len()

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
        self.p = p
        self.d1 = d1
        self.d2 = d2
    
    def normVec(self) -> Vector:
        '''
        Returns the normal vector to the plane.
        '''
        pass
    
    def angle(self, v: Vector) -> float:
        '''
        Returns the angle between the plane and a vector.
        '''
        pass



