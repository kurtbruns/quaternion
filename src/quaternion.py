import math
from .vector3 import Vector3

class Quaternion:

	def __init__(self, w: float, x: float, y: float, z: float):
		"""
		Construct a quaternion with components w, x, y, z.
		
		Args:
			w: The scalar (real) component of the quaternion.
			x: The x-component of the vector part.
			y: The y-component of the vector part.
			z: The z-component of the vector part.
		"""
		self.w = w
		self.x = x
		self.y = y
		self.z = z

	@staticmethod
	def from_axis_angle(axis: Vector3, angle: float) -> 'Quaternion':
		"""
		Construct a rotation quaternion from an axis and angle.
		
		Args:
			axis: The rotation axis vector (will be normalized if not unit length).
			angle: The rotation angle in radians.
			
		Returns:
			A new quaternion representing the rotation.
		"""

		if axis.length() != 1:
			axis = axis.normalize()

		half_angle = angle / 2
		
		return Quaternion(
			math.cos(half_angle),
			axis.x * math.sin(half_angle),
			axis.y * math.sin(half_angle),
			axis.z * math.sin(half_angle)
		)

	def multiply(self, other: 'Quaternion') -> 'Quaternion':
		"""
		Multiply this quaternion by another quaternion.
		
		Args:
			other: The quaternion to multiply by.
			
		Returns:
			A new quaternion representing the product.
		"""
		return Quaternion(
			self.w*other.w-self.x*other.x-self.y*other.y-self.z*other.z,
			self.w*other.x+self.x*other.w+self.y*other.z-self.z*other.y,
			self.w*other.y-self.x*other.z+self.y*other.w+self.z*other.x,
			self.w*other.z+self.x*other.y-self.y*other.x+self.z*other.w
		)

	def transform(self, v: Vector3) -> Vector3:
		"""
		Transform a vector by this quaternion.
		
		Args:
			v: The vector to transform.
			
		Returns:
			A new vector representing the transformed result.
		"""
		
		p = Quaternion(0, v.x, v.y, v.z)

		# Use the conjugate instead of inverse if working with unit quaternions
		t = (self.multiply(p)).multiply(self.inverse())

		return Vector3(t.x, t.y, t.z)

	def conjugate(self) -> 'Quaternion':
		"""
		Return the conjugate of this quaternion.
		
		Returns:
			A new quaternion representing the conjugate.
		"""
		return Quaternion(self.w, -self.x, -self.y, -self.z)

	def inverse(self) -> 'Quaternion':
		"""
		Return the inverse of this quaternion.
		
		Returns:
			A new quaternion representing the inverse.
		"""

		norm_squared = self.w**2+self.x**2+self.y**2+self.z**2

		return Quaternion(
			 self.w/norm_squared,
			-self.x/norm_squared,
			-self.y/norm_squared,
			-self.z/norm_squared
		)

	def copy(self) -> 'Quaternion':
		"""
		Returns a copy of this quaternion.
		
		Returns:
			A new quaternion with the same components as this one.
		"""
		return Quaternion(self.w, self.x, self.y, self.z)

	def scale(self, s: float) -> 'Quaternion':
		"""
		Scales the quaternion by a scalar.
		
		Args:
			s: The scalar value to multiply by.
			
		Returns:
			A new quaternion representing the scaled result.
		"""
		return Quaternion(s * self.w, s * self.x, s * self.y, s * self.z)

	def power(self, exponent: float) -> 'Quaternion':
		"""
		Raises this quaternion to the power of the given exponent.
				
		Args:
			exponent: The exponent to raise the quaternion to.
			
		Returns:
			A new quaternion representing the result of the exponentiation.
		"""
		# Compute the norm (magnitude) of the quaternion
		norm = math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)
		
		# Handle zero quaternion
		if norm < 1e-10:
			return Quaternion(0, 0, 0, 0)  # Zero quaternion
			
		norm_pow = norm**exponent
		
		# Compute the angle theta
		theta = math.acos(self.w / norm)
		
		# Compute the new scalar part
		new_w = norm_pow * math.cos(exponent * theta)
		
		# If the vector part is zero, return a scalar quaternion
		vector_magnitude = math.sqrt(self.x**2 + self.y**2 + self.z**2)
		if vector_magnitude < 1e-10:
			return Quaternion(new_w, 0, 0, 0)
		
		# Compute the new vector part
		factor = norm_pow * math.sin(exponent * theta) / vector_magnitude
		new_x = self.x * factor
		new_y = self.y * factor
		new_z = self.z * factor
		
		return Quaternion(new_w, new_x, new_y, new_z)

	def toString(self, precision: int = 2) -> str:
		"""
		Return a string representation of the quaternion with controlled precision.
		
		Args:
			precision: Number of decimal places to display (default: 2).
			
		Returns:
			A formatted string representation of the quaternion.
		"""
		# Lambda to format a component with proper sign
		format_component = lambda value, suffix: (
			f" {'-' if value < 0 else '+'} {abs(value):.{precision}f}{suffix}"
		)
		
		# Start with the scalar component
		result = f"{self.w:.{precision}f}"
		
		# Add vector components
		result += format_component(self.x, "i")
		result += format_component(self.y, "j") 
		result += format_component(self.z, "k")
		
		return result

	def __str__(self) -> str:
		"""
		Return a string representation of the quaternion (calls toString with default precision).
		
		Returns:
			A formatted string representation of the quaternion.
		"""
		return self.toString()

	def __repr__(self) -> str:
		"""
		Return a detailed string representation of the quaternion.
		
		Returns:
			A detailed string representation of the quaternion.
		"""
		return f"Quaternion({self.w}, {self.x}, {self.y}, {self.z})"


