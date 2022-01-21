class Vector3D:
    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if other is int:
            return Vector3D(self.x * other, self.y * other, self.z * other)
        #elif other is Vector3D:
            #return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)
    def __truediv__(self, other):
        if type(other) == int:
            return Vector2D(self.x / other, self.y / other)
    def __repr__(self) -> str:
        return f"Vector3D x:{self.x} y:{self.y} z:{self.z}"
    
class Vector2D:
    def __init__(self,x,y) -> None:
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
        
    def __truediv__(self, other):
        if type(other) == int:
            return Vector2D(self.x / other, self.y / other)
    def __repr__(self) -> str:
        return f"Vector2D x:{self.x} y:{self.y}"
    
if __name__ == "__main__":
    vec1 = Vector2D(2,0)
    vec2 = Vector2D(2,-2)
    vec3 = Vector2D(0,2)
    vec4 = Vector3D(2,4,9)
    print(vec1 / 2)
    
