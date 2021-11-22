# Class that provides a definition for the scene to be displayed by the renderer
class Scene:

	# Parametrised constructor to set up the scene
	def __init__(self,camera,objects,width,height):
		self.camera = camera
		self.objects = objects
		self.width = width
		self.height = height