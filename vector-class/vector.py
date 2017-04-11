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
        # the direction of the unit vector.
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
        return self.dotProduct(w) == 0.0

    def projection(self, b):
        # it is also the parallel component of a vector compared to b
        # the projection of v unto b = (v * unit vector b) * unit vector b
        unitB = b.direction()
        return unitB.scalarMultiply(self.dotProduct(unitB))

    def orthogonalComponent(self, b):
        # the orthogonal component is the vector minus its parallel one
        return self.minus(self.projection(b))

    def decompose(self, b):
        # i'm printing these here because when i return it,
        # i can't see the enitre vector within muy console
        print(self.projection(b), self.orthogonalComponent(b))
        return (self.projection(b), self.orthogonalComponent(b))

    def crossProduct(self, w):
        if len(self.coordinates) == 2:
            self.coordinates = [self.coordinates, 0]

        first = self.coordinates[1]*w.coordinates[2] - w.coordinates[1]*self.coordinates[2]
        second = self.coordinates[0]*w.coordinates[2] - w.coordinates[0]*self.coordinates[2]
        third = self.coordinates[0]*w.coordinates[1] - w.coordinates[0]*self.coordinates[1]

        return Vector([first, -second, third])

    def areaOfParallelogram(self, w):
        return self.crossProduct(w).magnitude()

    def areaOfTriangle(self, w):
        return self.crossProduct(w).magnitude() * .5

print(Vector([8.462, 7.893, -8.187]).crossProduct(Vector([6.984, -5.975, 4.778])))
print(Vector([-8.987, -9.838, 5.031]).areaOfParallelogram(Vector([-4.268, -1.861, -8.866])))
print(Vector([1.5, 9.547, 3.691]).areaOfTriangle(Vector([-6.007, .124, 5.772])))
