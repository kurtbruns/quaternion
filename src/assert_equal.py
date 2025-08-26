import pytest
from typing import Union
from .vector3 import Vector3
from .quaternion import Quaternion

def assert_equal(actual: Union[Vector3, Quaternion], expected: Union[Vector3, Quaternion]):
  """
  Compares two objects (Vector3 or Quaternion) for equality with 10 decimal place precision.
  
  Args:
    actual: The object to test (Vector3 or Quaternion)
    expected: The expected value (Vector3 or Quaternion)
  """
  if isinstance(actual, Vector3) and isinstance(expected, Vector3):
    assert actual.x == pytest.approx(expected.x, rel=1e-10)
    assert actual.y == pytest.approx(expected.y, rel=1e-10)
    assert actual.z == pytest.approx(expected.z, rel=1e-10)
  elif isinstance(actual, Quaternion) and isinstance(expected, Quaternion):
    assert actual.w == pytest.approx(expected.w, rel=1e-10)
    assert actual.x == pytest.approx(expected.x, rel=1e-10)
    assert actual.y == pytest.approx(expected.y, rel=1e-10)
    assert actual.z == pytest.approx(expected.z, rel=1e-10)
  else:
    raise TypeError("Both arguments must be of the same type (Vector3 or Quaternion)") 