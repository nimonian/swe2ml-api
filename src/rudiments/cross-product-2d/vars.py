import sympy as sp
import random
import src.utils as utils
from functools import reduce


def generate_vars():
    u = [random.randint(-10, 10) for _ in range(2)]
    v = [random.randint(-10, 10) for _ in range(2)]
    uv = u[0] * v[1] - v[0] * u[1]
    answer = abs(uv)

    return locals()
