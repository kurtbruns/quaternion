import math
from src.vector3 import Vector3
from src.quaternion import Quaternion
from demo_rotate import get_rotation_axis_and_angle

def slerp(q1: Quaternion, q2: Quaternion, t: float, shortestPath: bool = True) -> Quaternion:
    """
    Spherical linear interpolation between two quaternions.
    
    This implements SLERP as described in the script:
    1. Ensure shortest path by checking dot product (if shortestPath=True)
    2. Calculate rotation from q1 to q2
    3. Apply fraction of rotation using power method
    
    Args:
        q1: Starting quaternion
        q2: Ending quaternion
        t: Interpolation parameter (0 to 1)
        shortestPath: Whether to ensure shortest path (default: True)
        
    Returns:
        Interpolated quaternion
    """
    # Ensure shortest path if requested
    if shortestPath:
        # Calculate dot product: q1.w*q2.w + q1.x*q2.x + q1.y*q2.y + q1.z*q2.z
        dot_product = q1.w * q2.w + q1.x * q2.x + q1.y * q2.y + q1.z * q2.z
        if dot_product < 0:
            q2 = Quaternion(-q2.w, -q2.x, -q2.y, -q2.z)
    
    # Calculate the rotation from q1 to q2
    rotation = q2.multiply(q1.inverse())
    
    # Apply fraction of the rotation
    fraction_rotation = rotation.power(t)
    
    return fraction_rotation.multiply(q1)

def demo_slerp(shortestPath: bool = True, steps: int = 10):
    """
    Demo showing how SLERP interpolates between orientations.
    Uses two specific quaternions that would go the long way without ensuring shortest path.
    
    Args:
        shortestPath: Whether to ensure shortest path (default: True)
    """
    path_type = "Shortest Path" if shortestPath else "Long Path"
    print(f"\n--- SLERP {path_type} ---\n")
    
    # Two specific quaternions as provided
    q1 = Quaternion(0.6438, 0.4378, 0.2916, 0.5558)
    q2 = Quaternion(0.2232, -0.4233, -0.3139, -0.8201)
    
    print(f"\nInterpolating between q_1 and q_2\n")

    print(f"q_1={q1.toString()}")
    print(f"q_2={q2.toString()}")

    print(f"Ensure shortest path: {shortestPath}")

    
    # Calculate dot product for shortest path detection
    dot_product = q1.w * q2.w + q1.x * q2.x + q1.y * q2.y + q1.z * q2.z
    
    # Determine q2_for_rotation (might be negated to ensure shortest path)
    q2_for_rotation = q2
    if shortestPath:
        print(f"Dot product: {dot_product:.3f}")
        
        if dot_product < 0:
            q2_for_rotation = Quaternion(-q2.w, -q2.x, -q2.y, -q2.z)
            print(f"Dot product is negative, so negated q2 is closer: {q2_for_rotation.toString()}")
            print(f"Changing target quaternion q_2 to {q2_for_rotation.toString()}")
    
    total_rotation = q2_for_rotation.multiply(q1.inverse())
    total_axis, total_angle = get_rotation_axis_and_angle(total_rotation)
    total_angle_degrees = math.degrees(total_angle)
    print(f"Total rotation: {total_angle_degrees:.1f}° around axis {total_axis}\n")

    for i in range(steps + 1):
        t = i / steps
        q = slerp(q1, q2, t, shortestPath)
        print(f"t={t:.2f}: q={q}")

        # To calculate the transformed basis vectors, use the following:
        # q.transform(Vector3(1,0,0)) # transformed i-hat
        # q.transform(Vector3(0,1,0)) # transformed j-hat
        # q.transform(Vector3(0,0,1)) # transformed k-hat

        # To calculate the transformed point, use the following:
        # q.transform(Vector3(x,y,z))

        # This is how you can calculate the transformed position of all the points that make up a 3D object

    print()

if __name__ == "__main__":
    
    print("\n=== SLERP Demo ===\n")

    # Run demo
    demo_slerp(shortestPath=False)

    # Run demo and ensure shortest path
    demo_slerp(shortestPath=True)
