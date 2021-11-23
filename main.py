'''
A raytracer based on the Turner-Whitted paper
Done by: 
* Souporno S Ghosh
* Varun Peesapati
* Rishi Prakaash Srinivasan Mohan
* Venkatesh Vayachal
'''
import sys

from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from renderer import Renderer
from light import Light
from material import Material

def main():
	# Checking if the file name is passed as an argument
	if len(sys.argv) != 2:
		print("Correct usage: py main.py <filename>.ppm")
		sys.exit(1)

	output_file = sys.argv[1]

	# Setting up the scene and the renderer
	width = 320
	height = 200
	camera = Vector(0,0,-1)
	objects = [Sphere(Point(0,0,0),0.5,Material(Color.toRGB("#FF0000")))]
	lights = [Light(Point(1.5,-0.5,-10.0),Color.toRGB("#FFFFFF"))]
	scene = Scene(camera,objects,lights,width,height)
	renderer = Renderer()

	# Defining the image that has been rendered
	img = renderer.render(scene)

	with open(output_file,"w") as img_file:
		img.write_ppm(img_file)

if __name__ == "__main__":
	main()