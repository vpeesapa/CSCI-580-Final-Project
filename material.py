from color import Color

# Class that provides a definition of a material
class Material:

	# Parametrised constructor to initialize the material
	def __init__(self,color = Color.toRGB("#FFFFFF"),Ks = 1.0,Kd = 1.0,Ka = 0.05,reflection = 0.5):
		self.color = color
		self.Ks = Ks
		self.Kd = Kd
		self.Ka = Ka
		self.reflection = reflection

	# Function that returns the color of the material
	def get_color(self,position):
		return self.color

# Class that provides a definition for a checkerboard material
class Checkerboard:

	# Parametrised constructor to initialize the material
	def __init__(self,color1 = Color.toRGB("#FFFFFF"),color2 = Color.toRGB("#000000"),Ks = 1.0,Kd = 1.0,Ka = 0.05,reflection = 0.5):
		self.color1 = color1
		self.color2 = color2
		self.Ks = Ks
		self.Kd = Kd
		self.Ka = Ka
		self.reflection = reflection

	# Function that returns the appropriate color of the material
	def get_color(self,position):
		if int((position.x + 5.0) * 3.0) % 2 == int(position.z * 3.0) % 2:
			return self.color1
		else:
			return self.color2