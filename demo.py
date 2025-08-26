from src.vector3 import Vector3
from src.quaternion import Quaternion

# Create the quaternion from the test
q = Quaternion(0.83, 0.34, -0.44, 0.02)

# Create the basis vectors
i_hat = Vector3(1, 0, 0)
j_hat = Vector3(0, 1, 0)
k_hat = Vector3(0, 0, 1)

print(q.transform(i_hat))
print(q.transform(j_hat))
print(q.transform(k_hat))

import math

# Construct a rotation quaternion from an axis and angle
r = Quaternion.from_axis_angle(Vector3(0, 1, 0), math.pi/2)

# Apply the rotation
q = r.multiply(q)

print(q)

# %recall 7 8 9
print(q.transform(i_hat))
print(q.transform(j_hat))
print(q.transform(k_hat))
