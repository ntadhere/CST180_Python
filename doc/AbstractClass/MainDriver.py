from Circle import Circle
from Rectangle import Rectangle
from Triangle import Triangle

def Main():
    shapes = [
        Circle(5.0),
        Rectangle(4.0, 6.0),
        Triangle(3.0, 7.0)
    ]

    for shape in shapes:
        print(f"Area: {shape.area():.4f}")

Main()