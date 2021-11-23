# Class that provides a definition of a material
class Material:

	# Parametrised constructor to initialize the material
	def __init__(self,color,Ks = 1.0,Kd = 1.0,Ka = 0.05):
		self.color = color
		self.Ks = Ks
		self.Kd = Kd
		self.Ka = Ka

	# Function that returns the color of the material
	def get_color(self):
		return self.color