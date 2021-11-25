from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from light import Light
from material import Material,Checkerboard

# Declaring the scene essentials
width = 960
height = 540
rendered_image = "raytraced_image.ppm"
camera = Vector(0,-0.35,-1)
objects = [
	# Ground plane
	Sphere(Point(0,10000.5,1),10000.0,Checkerboard(Color.toRGB("#420500"),Color.toRGB("#e6b87d"),1.0,1.0,0.2,0.2)),
	# Blue ball
	Sphere(Point(0.75,-0.1,1),0.6,Material(Color.toRGB("#0000FF"))),
	# Purple ball
	Sphere(Point(-0.75,-0.1,2.25),0.6,Material(Color.toRGB("#803980")))
]
lights = [
	Light(Point(1.5,-0.5,-10),Color.toRGB("#FFFFFF")),
	Light(Point(-0.5,-10.5,0),Color.toRGB("#E6E6E6"))
]