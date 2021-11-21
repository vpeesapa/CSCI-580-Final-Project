from color import Color

# Class that defines a point-light source
class Light:

	# Parametrised constructor that defines the light source
	def __init__(self,position,color = Color.toRGB("#FFFFFF")):
		self.position = position
		self.color = color