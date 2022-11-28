from vector import Vector

print(Vector([[1., 2e-3, 3.14, 5.]]).values)

print(Vector(4).values)

try:
    Vector(-1)
except Exception as e:
    print(repr(e))

print(Vector((10, 12)).values)

try:
    print(Vector((3, 1)).values)
except Exception as e:
    print(repr(e))


try:
    v = Vector((1, 1))
    print(v.values)
except Exception as e:
    print(repr(e))

try:
    Vector((4, 7.1))
except Exception as e:
    print(repr(e))


print("**************************************************")

v = Vector(4)
print(v.values)

print(v * 4)

print(4.0 * v)

try:
    print(v * "hi")
except Exception as e:
    print(repr(e))

print("**************************************************")

v = Vector(4)
v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
print((v + v2).values)

try:
    print(v + Vector([[0.0, 0.0, 0.0, 0.0]]))
except Exception as e:
    print(repr(e))

try:
    print(v + "hello")
except Exception as e:
    print(repr(e))

try:
    print(v + None)
except Exception as e:
    print(repr(e))

print((v - v2).values != (v2 - v).values)

print("**************************************************")

print(Vector(4) / 2)
print(Vector(4) / 3.14)

try:
    print(Vector(4) / 0)
except Exception as e:
    print(repr(e))

try:
    print(Vector(4) / None)
except Exception as e:
    print(repr(e))

try:
    print(None / Vector(4))
except Exception as e:
    print(repr(e))

try:
    print(3 / Vector(3))
except Exception as e:
    print(repr(e))
