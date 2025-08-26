import math
from src.vector3 import Vector3
from src.quaternion import Quaternion

def project_on_sphere(touch_x, touch_y, width, height, r=0.5):
    """
    Projects 2D coordinates onto the surface of a unit sphere.
    
    Args:
        touch_x (float): X coordinate of the mouse input.
        touch_y (float): Y coordinate of the mouse input.
        width (float): Width of the viewport.
        height (float): Height of the viewport.
        r (float, optional): Radius of the virtual trackball.
        
    Returns:
        Vector3: A point on the unit sphere.
    """
    # Normalize to center and scale to height
    x = (touch_x - width / 2) / height
    y = -(touch_y - height / 2) / height  # Y-axis flipped
    
    distance_sq = x**2 + y**2
    
    if distance_sq <= (r * r / 2):
        # Inside the sphere - project onto sphere surface
        z = math.sqrt(r * r - distance_sq)
    else:
        # Outside the sphere - project onto hyperbolic surface
        z = (r * r / 2) / math.sqrt(distance_sq)
    
    return Vector3(x, y, z).normalize()

def calculate_rotation_between_points(p1: Vector3, p2: Vector3) -> Quaternion:
    """
    Calculates the rotation quaternion that rotates from point p1 to point p2.
    
    This implements the method described in the video:
    1. Convert points to quaternions with w=0
    2. Calculate q2 * q1.conjugate() 
    3. Raise to power 1/2 to get correct rotation angle
    
    Args:
        p1: Starting point on unit sphere
        p2: Ending point on unit sphere
        
    Returns:
        Quaternion representing the rotation from p1 to p2
    """
    # Convert points to quaternions with w=0
    q1 = Quaternion(0, p1.x, p1.y, p1.z)
    q2 = Quaternion(0, p2.x, p2.y, p2.z)
    
    # Calculate rotation: q2 * q1.conjugate()
    rotation = q2.multiply(q1.conjugate())
    
    # To divide the angle by 2, raise this result to power 1/2
    return rotation.power(0.5)

def get_rotation_axis_and_angle(q: Quaternion) -> tuple[Vector3, float]:
    """
    Extract the rotation axis and angle from a quaternion.
    
    This function assumes the quaternion represents a rotation (unit quaternion).
    For a quaternion q = cos(θ/2) + sin(θ/2)(xi + yj + zk), this returns:
    - axis: the normalized rotation axis (x, y, z)
    - angle: the rotation angle in radians
    
    Args:
        q: The quaternion representing a rotation
        
    Returns:
        A tuple of (axis, angle) where axis is a Vector3 and angle is in radians.
    """
    # Handle identity quaternion (no rotation)
    if abs(q.w) > 0.9999:
        return Vector3(0, 0, 1), 0.0
    
    # Calculate the angle
    angle = 2 * math.acos(q.w)
    
    # Calculate the axis (normalized)
    sin_half_angle = math.sqrt(1 - q.w * q.w)
    axis = Vector3(
        q.x / sin_half_angle,
        q.y / sin_half_angle,
        q.z / sin_half_angle
    )
    
    return axis, angle

def demo_simple_rotation():
    """
    Simple demo showing the core mouse drag rotation workflow.
    """
    print("=== Simple Mouse Drag Rotation Demo ===")
    
    # Initialize Earth orientation
    earth_orientation = Quaternion(1, 0, 0, 0)
    
    # Simulate viewport
    viewport_width = 960
    viewport_height = 540
    
    print("\n--- First Drag Event ---\n")
    
    # Show starting orientation for first drag
    print(f"Starting orientation: {earth_orientation.toString()}")
    
    # Show mouse positions
    mouse_start_x, mouse_start_y = 384, 432
    mouse_end_x, mouse_end_y = 653, 243
    print(f"Mouse start: ({mouse_start_x}, {mouse_start_y})")
    print(f"Mouse end: ({mouse_end_x}, {mouse_end_y})")
    
    # Show corresponding sphere points
    p1 = project_on_sphere(mouse_start_x, mouse_start_y, viewport_width, viewport_height)
    p2 = project_on_sphere(mouse_end_x, mouse_end_y, viewport_width, viewport_height)
    print(f"Sphere point 1: {p1}")
    print(f"Sphere point 2: {p2}")
    
    # Show calculated rotation
    rotation = calculate_rotation_between_points(p1, p2)
    print(f"Calculated rotation: {rotation.toString()}")
    axis, angle = get_rotation_axis_and_angle(rotation)
    angle_degrees = math.degrees(angle)
    print(f"Rotation description: Rotation by {angle_degrees:.1f}° around axis {axis}")
    
    # Apply rotation
    earth_orientation = rotation.multiply(earth_orientation)
    print(f"New orientation: {earth_orientation.toString()}")
    
    print("\n--- Second Drag Event ---\n")
    
    # Show starting orientation for second drag
    print(f"Starting orientation: {earth_orientation.toString()}")
    
    # Show one more drag event
    mouse_start_x2, mouse_start_y2 = 355, 119
    mouse_end_x2, mouse_end_y2 = 317, 313
    print(f"Mouse start: ({mouse_start_x2}, {mouse_start_y2})")
    print(f"Mouse end: ({mouse_end_x2}, {mouse_end_y2})")
    
    p1_2 = project_on_sphere(mouse_start_x2, mouse_start_y2, viewport_width, viewport_height)
    p2_2 = project_on_sphere(mouse_end_x2, mouse_end_y2, viewport_width, viewport_height)
    print(f"Sphere point 1: {p1_2}")
    print(f"Sphere point 2: {p2_2}")
    
    rotation2 = calculate_rotation_between_points(p1_2, p2_2)
    print(f"Calculated rotation: {rotation2.toString()}")
    axis, angle = get_rotation_axis_and_angle(rotation2)
    angle_degrees = math.degrees(angle)
    print(f"Rotation description: Rotation by {angle_degrees:.1f}° around axis {axis}")
    
    earth_orientation = rotation2.multiply(earth_orientation)
    print(f"Final orientation: {earth_orientation.toString()}")

if __name__ == "__main__":
    demo_simple_rotation()