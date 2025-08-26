import math

class Vector3:
  """
  Represents a three-dimensional vector.
  """
  
  def __init__(self, x: float = 0, y: float = 0, z: float = 0):
    """
    Constructs a new Vector3 instance.
    
    Args:
      x: The x-component of the vector.
      y: The y-component of the vector.
      z: The z-component of the vector.
    """
    self.x = x
    self.y = y
    self.z = z
  
  def copy(self) -> 'Vector3':
    """
    Returns a copy of this vector.
    """
    return Vector3(self.x, self.y, self.z)
  
  def set(self, v: 'Vector3') -> None:
    """
    Sets this vector equal to the provided vector.
    """
    self.x = v.x
    self.y = v.y
    self.z = v.z

  def add(self, v: 'Vector3') -> 'Vector3':
    """
    Adds this vector to another vector.
    
    Args:
      v: The vector to add.
      
    Returns:
      A new Vector3 representing the sum of the two vectors.
    """
    return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)
  
  def subtract(self, v: 'Vector3') -> 'Vector3':
    """
    Subtracts another vector from this vector.
    
    Args:
      v: The vector to subtract.
      
    Returns:
      A new Vector3 representing the difference.
    """
    return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)
  
  def scale(self, s: float) -> 'Vector3':
    """
    Scales the vector by a scalar value.
    
    Args:
      s: The scalar value
      
    Returns:
      A new Vector3 representing the scaled vector.
    """
    return Vector3(
      s * self.x,
      s * self.y,
      s * self.z
    )
  
  def inverse(self) -> 'Vector3':
    """
    Returns a new Vector3 representing the inverse of this vector.
    """
    return Vector3(-self.x, -self.y, -self.z)

  def length(self) -> float:
    """
    Calculates the length of this vector.
    
    Returns:
      The length of the vector.
    """
    return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
  
  def is_zero(self) -> bool:
    """
    Checks if the vector is a zero vector (all components are 0).
    
    Returns:
      True if the vector is a zero vector, False otherwise.
    """
    return self.x == 0 and self.y == 0 and self.z == 0

  def dot(self, v: 'Vector3') -> float:
    """
    Calculates the dot product of this vector with another vector.
    
    Args:
      v: The other vector.
      
    Returns:
      The dot product as a float.
    """
    return self.x * v.x + self.y * v.y + self.z * v.z
  
  def cross(self, v: 'Vector3') -> 'Vector3':
    """
    Calculates the cross product of this vector with another vector.
    
    Args:
      v: The other vector.
      
    Returns:
      A new Vector3 representing the cross product.
    """
    return Vector3(
      self.y * v.z - self.z * v.y,
      self.z * v.x - self.x * v.z,
      self.x * v.y - self.y * v.x
    )
  
  def normalize(self) -> 'Vector3':
    """
    Normalizes the vector, resulting in a unit vector.
    
    Returns:
      A new Vector3 representing the normalized vector.
    """
    length = self.length()
    return Vector3(self.x / length, self.y / length, self.z / length)

  def __iter__(self):
    """
    Yields the components of the vector.
    """
    yield self.x
    yield self.y
    yield self.z
  
  def __str__(self) -> str:
    """
    Returns a string representation of the vector in the format [x, y, z].
    Components are rounded to 3 decimal places.
    """
    return f"[{self.x:.3f}, {self.y:.3f}, {self.z:.3f}]" 