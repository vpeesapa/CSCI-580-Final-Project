import math

# Class that defines a vector and its basic operations
class Vector:
	# Parametrised constructor that defines the vector
	def __init__(self,x = 0.0,y = 0.0,z = 0.0):
		self.x = x
		self.y = y
		self.z = z

	# Function that measures the magnitude of the vector
	def magnitude(self):
		return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

	# Function that calculates the dot product of two vectors
	def dot_product(self,vector2):
		return self.x * vector2.x + self.y * vector2.y + self.z * vector2.z

	# Function that calculates the cross product of two vectors
	def cross_product(self,vector2):
		newX = (self.y * vector2.z) - (self.z * vector2.y)
		newY = (self.z * vector2.x) - (self.x * vector2.z)
		newZ = (self.x * vector2.y) - (self.y * vector2.x)

		return Vector(newX,newY,newZ)

	# Function that normalizes the vector
	def normalize(self):
		magnitude = self.magnitude()
		
		return self.divide_scalar(magnitude)

	# Function that multiplies the vector by a scalar
	def multiply_scalar(self,scalar):
		return Vector(self.x * scalar,self.y * scalar,self.z * scalar)

	# Function that divides the vector by a scalar
	def divide_scalar(self,scalar):
		return Vector(self.x / scalar,self.y / scalar,self.z / scalar)

	# Overloaded function that adds two vectors
	def __add__(self,vector2):
		newX = self.x + vector2.x
		newY = self.y + vector2.y
		newZ = self.z + vector2.z

		return Vector(newX,newY,newZ)

	# Overloaded function that subtracts the second vector from the first vector
	def __sub__(self,vector2):
		newX = self.x - vector2.x
		newY = self.y - vector2.y
		newZ = self.z - vector2.z

		return Vector(newX,newY,newZ)

	# Overloaded function that formats the vector into a string for easy-to-use printing
	def __str__(self):
		return "({},{},{})".format(self.x,self.y,self.z)