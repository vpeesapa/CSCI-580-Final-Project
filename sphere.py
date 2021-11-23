import math

# Class that provides a definition for a sphere
class Sphere:

	# Parametrised constructor to initialize the sphere
	def __init__(self,center,radius,material):
		self.center = center
		self.radius = radius
		self.material = material

	# Function that checks if a ray intersects with the sphere
	def intersects(self,ray):
		sphere_to_ray = ray.origin - self.center

		# Calculate the discriminant which determines if the ray is intersecting with the sphere or not
		a = 1
		b = 2 * (ray.direction.dot_product(sphere_to_ray))
		c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius ** 2

		discriminant = b ** 2 - 4 * a * c

		if discriminant >= 0:
			distance = (-b - math.sqrt(discriminant)) / (2 * a)

			if distance > 0:
				return distance

		return None

	# Function that returns the normal at a point on the surface
	def normal(self,surface_point):
		return (surface_point - self.center).normalize()