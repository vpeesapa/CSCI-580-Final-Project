from color import Color

class Light:
	def __init__(self,position,color = Color.toRGB("#FFFFFF")):
		self.position = position
		self.color = color