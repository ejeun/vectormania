import math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, addor):
        # to add, we want to take the first index of the tuple and add it
        # then add the second index and add
        # create a new vector with those values as coords
        sum = []
        for i in range(len(self.coordinates)):
            sum.append(self.coordinates[i] + addor.coordinates[i])
        return Vector(tuple(sum))

    def minus(self, subtractor):
        diff = []
        for i in range(len(self.coordinates)):
            diff.append(self.coordinates[i] - subtractor.coordinates[i])
        return Vector(tuple(diff))

    def scalarMultiply(self, multiplier):
        # for each item in the tuple, multiply it..
        products = []
        for i in range(len(self.coordinates)):
            products.append(self.coordinates[i] * multiplier)
        return Vector(tuple(products))

    def magnitude(self):
        # magnitude = (x^2 + y^2) ^ 1/2
        coords = []
        for i in range(len(self.coordinates)):
            coords.append((self.coordinates[i]) ** 2)
        return sum(coords) ** (1 / 2)

    def direction(self):
        # direction = 1 / magnitude * vector
        return self.scalarMultiply(1 / self.magnitude())

    def dotProduct(self, w):
        # v (dot) w = v1w1 + v2w2 + ... vnwn
        # except when one of them is zero...
        coords = []
        for i in range(len(self.coordinates)):
            coords.append(self.coordinates[i] * w.coordinates[i])
        return round(sum(coords), 3)

    def angle(self, w, dot, rad):
        # angle takes 3 params. w: a Vector,
        # dot: boolean for using dot or cross
        # and rad: booleans for retuning degrees or radian
        if dot:
            # the dot product = magnitude of v * magnitude of w * cos
            dotP = self.dotProduct(w)
            divisor = self.magnitude() * w.magnitude()
            cosTheta = dotP / divisor
            result = math.acos(cosTheta)

        if rad:
            return result
        elif not rad:
            result = result * 180 / math.pi
            return result

    def checkParallel(self, w):
        # if v is a scalar multiple of w, return true
        if w.coordinates[0] == 0:
            # if its zero... check if everything is zero
            for i in range(len(w.coordinates)):
                if w.coordinates[i] != 0:
                    return False
            return True
        # otherwise, continue business as usual
        multiple = w.coordinates[0] / self.coordinates[0]
        return self.scalarMultiply(multiple) == w

    def checkOrthogonal(self, w):
        # if the dot product is 0, then its orthogonal
        return self.dotProduct(w) == 0


# 4. quiz: parallel or orthogonal
print(Vector([-7.579, -7.88]).checkParallel(Vector([22.737, 23.64])))
print(Vector([-7.579, -7.88]).checkOrthogonal(Vector([22.737, 23.64])))

print(Vector([-2.029, 9.97, 4.172]).checkParallel(Vector([-9.231, -6.639, -7.245])))
print(Vector([-2.029, 9.97, 4.172]).checkOrthogonal(Vector([-9.231, -6.639, -7.245])))

print(Vector([-2.328, -7.284, -1.214]).dotProduct(Vector([-1.821, 1.072, -2.94])))
print(Vector([-2.328, -7.284, -1.214]).checkOrthogonal(Vector([-1.821, 1.072, -2.94])))

print(Vector([2.118, 4.827]).checkParallel(Vector([0, 0])))
print(Vector([2.118, 4.827]).checkOrthogonal(Vector([0, 0])))
