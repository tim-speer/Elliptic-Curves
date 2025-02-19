from checks import check_curve, discriminant, check_int_point


class EllipticCurve:

    def __init__(self, a, b):
        check_curve(a, b)
        self._a = a
        self._b = b
        self._solutions = []
        self._level = 0

    def __call__(self, x, y):
        check_int_point(x, y)
        return y ** 2 - x ** 3 - self._a * x - self._b

    def discriminant(self):
        return discriminant(self._a, self._b)

    def is_solution(self, x, y):
        return self(x, y) == 0

    def _search(self, level):
        points = points_at_level(level)

        for point in points:
            if self.is_solution(point[0], point[1]):
                self._solutions.append(point)

    def find_solutions(self, num_levels=1):
        for i in range(num_levels):
            self._search(self._level)
            self._level += 1


def points_at_level(level):
    if level == 0:
        return [(0, 0)]

    points = []
    for y in range(-level, level + 1):
        points += [(-level, y), (level, y)]
    
    for x in range(1 - level, level):
        points += [(x, -level), (x, level)]

    return points     
