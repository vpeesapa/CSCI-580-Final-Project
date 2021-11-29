'''
A raytracer based on the Turner-Whitted paper
Done by: 
* Souporno S Ghosh
* Varun Peesapati
* Rishi Prakaash Srinivasan Mohan
* Venkatesh Vayachal
'''
import sys
import importlib
import os

from datetime import datetime
from scene import Scene
from renderer import Renderer

def main():
	# Checking if the file name is passed as an argument
	if len(sys.argv) != 2:
		print("Correct usage: py main.py <setup_script>")
		sys.exit(1)

	path_to_setup = sys.argv[1]
	mod = importlib.import_module(path_to_setup)

	# Creating a time stamp to test the speed of our program
	current_time = datetime.now()
	current_time = current_time.strftime("%H:%M:%S")

	print("Start time:",current_time)

	# Rendering the scene
	scene = Scene(mod.camera,mod.objects,mod.lights,mod.width,mod.height)
	renderer = Renderer()
	image = renderer.render(scene)

	os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
	with open(mod.rendered_image,"w") as img_file:
		image.write_ppm(img_file)

	current_time = datetime.now()
	current_time = current_time.strftime("%H:%M:%S")

	print("End time:",current_time)

if __name__ == "__main__":
	main()