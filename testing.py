import unittest
from Vectors import Vector3D

class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector3D(1.0, -2.0, -2.0)
    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)
        
if __name__ == '__main__':
    unittest.main()