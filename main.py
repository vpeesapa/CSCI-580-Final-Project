'''
A raytracer based on the Turner-Whitted paper
Done by: 
* Souporno S Ghosh
* Varun Peesapati
* Rishi Prakaash Srinivasan Mohan
* Venkatesh Vayachal
'''

from image import Image
from color import Color

def main():
	# Defining the image
	width = 3
	height = 2
	img = Image(width,height)

	# Defining the color
	red = Color(x = 1,y = 0,z = 0)
	green = Color(x = 0,y = 1,z = 0)
	blue = Color(x = 0,y = 0,z = 1)

	# Setting the colors to the image
	img.set_pixel(0,0,red)
	img.set_pixel(1,0,green)
	img.set_pixel(2,0,blue)

	img.set_pixel(0,1,red + green)
	img.set_pixel(1,1,red + blue + green)
	img.set_pixel(2,1,red.multiply_scalar(0.001))

	with open("test.ppm","w") as img_file:
		img.write_ppm(img_file)

if __name__ == "__main__":
	main()