from cmath import sqrt


class Vector3D:
    """3D Vector Element"""
    def __init__(self,x=0.0,y=0.0,z=0.0) -> None:
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if other is int:
            return Vector3D(self.x * other, self.y * other, self.z * other)
        #elif other is Vector3D:
            #return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)
    def __rmul__(self, other):
        if other is int:
            return Vector3D(self.x * other, self.y * other, self.z * other)
        #elif other is Vector3D:
            #return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)
    def __truediv__(self, other):
        if type(other) == int:
            return Vector3D(self.x / other, self.y / other, self.z / other)
    def __repr__(self) -> str:
        return f"Vector3D x:{self.x} y:{self.y} z:{self.z}"
    def magnitude(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def normalize(self):
        return self/self.magnitude()
    
class Vector2D:
    """"2D Vector Element"""
    def __init__(self,x=0.0,y=0.0,z=0.0) -> None:
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        if type(other) == int:
            return Vector2D(self.x * other, self.y * other)
        #elif type(other) == Vector2D:
            #return Vector2D(self.x * other.x, self.y * other.y)
    def __rmul__(self, other):
        if type(other) == int:
            return Vector2D(self.x * other, self.y * other)
        #elif type(other) == Vector2D:
            #return Vector2D(self.x * other.x, self.y * other.y)
        
    def __truediv__(self, other):
        if type(other) == int:
            return Vector2D(self.x / other, self.y / other)
    def __repr__(self) -> str:
        return f"Vector2D x:{self.x} y:{self.y}"
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def magnitude(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y
    def normalize(self):
        return self/self.magnitude()
    
if __name__ == "__main__":
    vec1 = Vector2D(2,0)
    vec2 = Vector2D(2,-2)
    vec3 = Vector2D(0,2)
    vec4 = Vector3D(1,-2,-2)
    print(vec4.magnitude())
    
