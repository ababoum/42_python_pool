'''
Test examples for class Vector
'''

from vector import Vector

# Column vector of shape n * 1
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v2)
# Expected output:
# Vector([[0.0], [5.0], [10.0], [15.0]])
# Row vector of shape 1 * n
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(v2)
# Expected output
# Vector([[0.0, 5.0, 10.0, 15.0]])
v2 = v1 / 2.0
print(v2)
# Expected output
# Vector([[0.0], [0.5], [1.0], [1.5]])
v2 = v1 / 2
print(v2)
# Expected output
# Vector([[0.0], [0.5], [1.0], [1.5]])
try:
    print(v1 / 0.0)
except Exception as e:
    print(repr(e))
# Expected ouput
# ZeroDivisionError: division by zero.
try:
    print(2.0 / v1)
except Exception as e:
    print(repr(e))
# Expected output:
# NotImplementedError: Division of a scalar by a Vector is not defined here.


# Column vector of shape (n, 1)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
# Expected output
# (4,1)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
# Expected output
# [[0.0], [1.0], [2.0], [3.0]]
# Row vector of shape (1, n)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
# Expected output
# (1,4)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
# Expected output
# [[0.0, 1.0, 2.0, 3.0]]
print("\033[93mExample 1:\033[0m")
# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape)
# Expected output:
# (4, 1)
print(v1.T())
# Expected output:
# Vector([[0.0, 1.0, 2.0, 3.0]])
print(v1.T().shape)
# Expected output:
# (1,4)
print("\033[93mExample 2:\033[0m")
# Example 2:
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shape)
# Expected output:
# (1,4)
print(v2.T())
# Expected output:
# Vector([[0.0], [1.0], [2.0], [3.0]])
print(v2.T().shape)
# Expected output:
# (4,1)
print("\033[93mExample 3:\033[0m")
# Example 3:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
# Expected output:
# 18.0
v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))
# Expected output:
# 13.0
print(repr(v1))
# Expected output: to see what __repr__() should do
# [[0.0, 1.0, 2.0, 3.0]]
print(v1)
# Expected output: to see what __str__() should do
# [[0.0, 1.0, 2.0, 3.0]]
print("\033[93mExample 4:\033[0m")
print(Vector(size=3))
print(Vector(_range=(10, 16)))
try:
    print(Vector(_range=(18, 16)))
except Exception as e:
    print(repr(e))