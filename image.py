# Function that converts a value to its 8-bit equivalent
def to_byte(c):
	return round(max(min(c * 255,255),0))

# Class that defines and creates an image
class Image:

	# Parametrised constructor to define the image
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.pixels = [[None for _ in range(width)] for _ in range(height)]

	# Function that sets pixel[y][x] with color
	def set_pixel(self,x,y,color):
			self.pixels[y][x] = color

	# Function that writes to the ppm file
	def write_ppm(self,img_file):
		# Writing the header of the image file
		img_file.write("P3 {} {} 255\n".format(self.width,self.height))

		# Writing the colors into the image file
		for row in self.pixels:
			for color in row:
				img_file.write("{} {} {} ".format(to_byte(color.x),to_byte(color.y),to_byte(color.z)))

			img_file.write("\n")