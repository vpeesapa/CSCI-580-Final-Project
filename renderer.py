from image import Image
from ray import Ray
from point import Point
from color import Color

# Class that provides a definition for the renderer
class Renderer:

	# Function that renders the image
	def render(self,scene):
		width = scene.width
		height = scene.height
		aspect_ratio = float(width) / height

		# Setting the boundaries for the scene
		x_min = -1.0
		x_max = 1.0
		dx = (x_max - x_min) / (width - 1)

		y_min = -1.0 / aspect_ratio
		y_max = 1.0 / aspect_ratio
		dy = (y_max - y_min) / (height - 1)

		camera = scene.camera
		pixels = Image(width,height)

		for j in range(height):
			y = y_min + j * dy

			for i in range(width):
				x = x_min + i * dx
				ray = Ray(camera,Point(x,y,0) - camera)

				# Render the image one pixel at a time
				pixels.set_pixel(i,j,self.ray_trace(ray,scene))

		return pixels

	# Function that traces the ray from the image to the eye
	def ray_trace(self,ray,scene):
		color = Color(0,0,0)

		# Finding the nearest object hit by the ray in the scene
		distance_hit,object_hit = self.find_nearest(ray,scene)

		if object_hit is None:
			# If the ray does not intersect any sphere, return the default color
			return color

		hit_pos = ray.origin + ray.direction.multiply_scalar(distance_hit)
		normal_hit = object_hit.normal(hit_pos)
		color += self.get_color(object_hit,hit_pos,normal_hit,scene)

		return color

	# Function that finds the nearest object hit by the ray in the scene
	def find_nearest(self,ray,scene):
		min_distance = None
		object_hit = None

		for obj in scene.objects:
			distance = obj.intersects(ray)

			# Check if the ray is hitting the sphere
			if distance is not None and (object_hit is None or distance < min_distance):
				min_distance = distance
				object_hit = obj

		return min_distance,object_hit

	# Function that calculates the color at a certain pixel
	def get_color(self,object_hit,hit_pos,normal,scene):
		material = object_hit.material
		object_color = material.get_color()
		to_camera = scene.camera - hit_pos
		specular_k = 50
		color = Color.toRGB("#000000").multiply_scalar(material.Ka)

		# Calculate the shading
		for light in scene.lights:
			to_light = Ray(hit_pos,light.position - hit_pos)

			# Diffuse shading
			color += object_color.multiply_scalar(material.Kd * max(normal.dot_product(to_light.direction),0))

			# Specular shading using the Blinn-Phong model
			half_vector = (to_light.direction + to_camera).normalize()
			color += light.color.multiply_scalar(material.Ks * (max(normal.dot_product(half_vector),0) ** specular_k))

		return color