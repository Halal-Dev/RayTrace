#!usr
"""Puray - Pure Python Ray Tracing algorithm written by Y"""
from image import Image
from color import Color
from Vectors import Vector3D
def main():
    WIDTH = 320
    HEIGHT = 200
    camera = Vector3D(0,0,-1)
    objects = [Sphere(Point(0,0,0), 0.5), Color.from_hex("#FF0000")]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)
    with open("test.ppm", 'w') as img_file:
        image.write_ppm(img_file)

if __name__ == "__main__":
    main()