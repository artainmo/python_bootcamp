from vector import *

v1 = Vector([0.0, 1.0, 2.0, 3.0])
print(v1.values)
v1.__add__(5)
print(v1.values)
print("==========")
print(v1.values)
v1.__radd__([2, 3, 4, 1])
print(v1.values)
