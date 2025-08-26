import math
from .vector3 import Vector3
from .quaternion import Quaternion
from .assert_equal import assert_equal

def test_rotation():

	q = Quaternion(1, 0, 0, 0)

	i_hat = Vector3(1, 0, 0)
	j_hat = Vector3(0, 1, 0)
	k_hat = Vector3(0, 0, 1)

	assert_equal(q.transform(i_hat), Vector3(1, 0, 0))
	assert_equal(q.transform(j_hat), Vector3(0, 1, 0))
	assert_equal(q.transform(k_hat), Vector3(0, 0, 1))

	a = Quaternion.from_axis_angle(Vector3(1, 0, 0), math.pi/2)

	b = Quaternion.from_axis_angle(Vector3(1, 1, 1), -2*math.pi/3)

	q = a.multiply(q)

	assert_equal(q.transform(i_hat), Vector3(1, 0, 0))
	assert_equal(q.transform(j_hat), Vector3(0, 0, 1))
	assert_equal(q.transform(k_hat), Vector3(0, -1, 0))

	q = b.multiply(q)

	assert_equal(q.transform(i_hat), Vector3(0, 0, 1))
	assert_equal(q.transform(j_hat), Vector3(0, 1, 0))
	assert_equal(q.transform(k_hat), Vector3(-1, 0, 0))

def test_rotation_other_way():

	q = Quaternion(1, 0, 0, 0)

	i_hat = Vector3(1, 0, 0)
	j_hat = Vector3(0, 1, 0)
	k_hat = Vector3(0, 0, 1)

	assert_equal(q.transform(i_hat), Vector3(1, 0, 0))
	assert_equal(q.transform(j_hat), Vector3(0, 1, 0))
	assert_equal(q.transform(k_hat), Vector3(0, 0, 1))

	a = Quaternion.from_axis_angle(Vector3(1, 0, 0), math.pi/2)

	b = Quaternion.from_axis_angle(Vector3(1, 1, 1), -2*math.pi/3)

	q = b.multiply(q)

	assert_equal(q.transform(i_hat), Vector3(0, 0, 1))
	assert_equal(q.transform(j_hat), Vector3(1, 0, 0))
	assert_equal(q.transform(k_hat), Vector3(0, 1, 0))

	q = a.multiply(q)

	assert_equal(q.transform(i_hat), Vector3(0, -1, 0))
	assert_equal(q.transform(j_hat), Vector3(1, 0, 0))
	assert_equal(q.transform(k_hat), Vector3(0, 0, 1))

def test_multiply():

	i = Quaternion(0, 1, 0, 0)
	j = Quaternion(0, 0, 1, 0)
	k = Quaternion(0, 0, 0, 1)

	# i² = -1
	assert_equal(i.multiply(i), Quaternion(-1, 0, 0, 0))
	
	# j² = -1
	assert_equal(j.multiply(j), Quaternion(-1, 0, 0, 0))

	# k² = -1
	assert_equal(k.multiply(k), Quaternion(-1, 0, 0, 0))

	# i⋅j = k
	assert_equal(i.multiply(j), Quaternion(0, 0, 0, 1))

	# j⋅k = i
	assert_equal(j.multiply(k), Quaternion(0, 1, 0, 0))

	# k⋅i = j
	assert_equal(k.multiply(i), Quaternion(0, 0, 1, 0))

	# j⋅i = -k
	assert_equal(j.multiply(i), Quaternion(0, 0, 0, -1))

	# k⋅j = -i
	assert_equal(k.multiply(j), Quaternion(0, -1, 0, 0))

	# i⋅k = -j
	assert_equal(i.multiply(k), Quaternion(0, 0, -1, 0))

	# i⋅j⋅k = -1
	assert_equal(i.multiply(j).multiply(k), Quaternion(-1, 0, 0, 0))

def test_power_for_rotations():
		
	# Create a 90-degree rotation around z-axis
	q = Quaternion.from_axis_angle(Vector3(0, 0, 1), math.pi/2)
	
	# Test q^0 = identity (no rotation)
	q_power_0 = q.power(0)
	assert_equal(q_power_0, Quaternion(1, 0, 0, 0))
	
	# Test q^1 = q (full rotation)
	q_power_1 = q.power(1)
	assert_equal(q_power_1, q)
	
	# Test q^2 = q * q (double rotation = 180 degrees)
	q_power_2 = q.power(2)
	q_squared = q.multiply(q)
	assert_equal(q_power_2, q_squared)
	
	# Another way to test q^2 = q * q (double rotation = 180 degrees)
	expected_double = Quaternion.from_axis_angle(Vector3(0, 0, 1), math.pi)
	assert_equal(q_power_2, expected_double)
	
	# Test q^0.5 = sqrt(q) (half rotation = 45 degrees)
	q_power_half = q.power(0.5)
	expected_half = Quaternion.from_axis_angle(Vector3(0, 0, 1), math.pi/4)
	assert_equal(q_power_half, expected_half)
