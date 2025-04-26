import sympy as sp
import random
import src.utils as utils


def generate_vars():
    u = [random.randint(-10, 10) for _ in range(3)]
    v = [random.randint(-10, 10) for _ in range(3)]
    w = [random.randint(-10, 10) for _ in range(3)]

    vw = [
        v[1] * w[2] - w[1] * v[2],
        v[2] * w[0] - w[2] * v[0],
        v[0] * w[1] - w[0] * v[1],
    ]

    A = u[0] * (v[1] * w[2] - w[1] * v[2])
    B = u[1] * (v[2] * w[0] - w[2] * v[0])
    C = u[2] * (v[0] * w[1] - w[0] * v[1])

    answer = abs(A + B + C)
    return locals()
