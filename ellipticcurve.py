from checks import check_curve, discriminant, check_int_point


class EllipticCurve:

    def __init__(self, a, b):
        check_curve(a, b)
        self._a = a
        self._b = b
        self._solutions = []

    def __call__(self, x, y):
        check_int_point(x, y)
        return y ** 2 - x ** 3 - self._a * x - self._b

    def discriminant(self):
        return discriminant(self._a, self._b)

    def is_solution(self, x, y):
        return self(x, y) == 0
