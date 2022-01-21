class Vector3D:
    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
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
    def __repr__(self) -> str:
        return f"Vector2D x:{self.x} y:{self.y}"
    
if __name__ == "__main__":
    vec1 = Vector2D(2,0)
    vec2 = Vector2D(2,-2)
    vec3 = Vector2D(0,2)
    print(vec1 + vec2 - vec3)
    
