def discriminant(a, b):
    return 4 * (a ** 3) + 27 * (b ** 2)


def check_singular(a, b):
    if discriminant(a, b) == 0:
        raise ValueError(f'({a}, {b}) defines a singular curve')


def check_type(var, valid_type):
    if not isinstance(var, valid_type):
        raise TypeError(f'{var} needs to have type {valid_type}')


def check_curve(a, b):
    check_type(a, int)
    check_type(b, int)
    check_singular(a, b)


def check_int_point(x, y):
    check_type(x, int)
    check_type(y, int)
