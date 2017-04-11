# hey = Vector([1, 2])
# print(hey.plus(Vector([10, 1])))
# print(hey.scalarMultiply(3))
# print(hey.minus(Vector([10, 1])))
# print(hey)
# print(hey.__eq__(Vector([1, 0])))

# 1. quiz: plus, minus, multiply
# print(Vector([8.218, -9.341]).plus(Vector([-1.129, 2.111])))
# print(Vector([7.119, 8.215]).minus(Vector([-8.223, 0.878])))
# print(Vector([1.671, -1.012, -0.318]).scalarMultiply(7.41))

# 2. quiz: magnitude, normalization
# print(Vector([-0.221, 7.437]).magnitude())
# print(Vector([8.813, -1.331, -6.247]).magnitude())
# print(Vector([5.581, -2.136]).direction())
# print(Vector([1.996, 3.108, -4.554]).direction())

# 3. quiz: dot products
# print(Vector([7.887, 4.138]).dotProduct(Vector([-8.802, 6.776])))
# print(Vector([-5.955, -4.904, -1.874]).dotProduct(Vector([-4.496, -8.755, 7.103])))
# print(Vector([3.183, -7.627]).angle(Vector([-2.668, 5.319]), True, True))
# print(Vector([7.35, 0.221, 5.188]).angle(Vector([2.751, 8.259, 3.985]), True, False))


# 4. quiz: parallel or orthogonal
# print(Vector([-7.579, -7.88]).checkParallel(Vector([22.737, 23.64])))
# print(Vector([-7.579, -7.88]).checkOrthogonal(Vector([22.737, 23.64])))

# print(Vector([-2.029, 9.97, 4.172]).checkParallel(Vector([-9.231, -6.639, -7.245])))
# print(Vector([-2.029, 9.97, 4.172]).checkOrthogonal(Vector([-9.231, -6.639, -7.245])))

# print(Vector([-2.328, -7.284, -1.214]).checkParallel(Vector([-1.821, 1.072, -2.94])))
# print(Vector([-2.328, -7.284, -1.214]).checkOrthogonal(Vector([-1.821, 1.072, -2.94])))

# print(Vector([2.118, 4.827]).checkParallel(Vector([0, 0])))
# print(Vector([2.118, 4.827]).checkOrthogonal(Vector([0, 0])))


# 5. quiz: projection, orthogonal, decomposition

# print(Vector([3.039, 1.879]).projection(Vector([0.825, 2.036])))
# print(Vector([-9.88, -3.264, -8.159]).orthogonalComponent(Vector([-2.155, -9.353, -9.473])))
# print(Vector([3.009, -6.172, 3.692, -2.51]).decompose(Vector([6.404, -9.144, 2.759, 8.718])))
