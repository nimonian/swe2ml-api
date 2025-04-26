import sympy as sp
import random
import src.utils as utils
from functools import reduce
from decimal import Decimal


def generate_vars():
    u = [random.randint(-10, 10) for _ in range(3)]
    v = [random.randint(-10, 10) for _ in range(3)]

    yz = u[1] * v[2] - u[2] * v[1]
    zx = u[2] * v[0] - u[0] * v[2]
    xy = u[0] * v[1] - u[1] * v[0]

    answer = yz + zx + xy

    return locals()
