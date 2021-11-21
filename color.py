from vector import Vector

# Class that stores the color
class Color(Vector):

	# Function that converts a color from hexadecimal string to r,g, and b values
	@classMethod
	def toRGB(cls,color = "#000000"):
		red = int(color[1:3],16) / 255.0
		blue = int(color[3:5],16) / 255.0
		green = int(color[5:7],16) / 255.0

		return cls(red,blue,green)