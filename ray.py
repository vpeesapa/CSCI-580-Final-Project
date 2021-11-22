# Class that provides a definition for a ray
class Ray:

	# Parametrised constructor to initialize a ray
	def __init__(self,origin,direction):
		self.origin = origin
		self.direction = direction.normalize()