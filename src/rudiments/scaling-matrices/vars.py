import sympy as sp
import random
import src.utils as utils


def generate_vars():
    m = random.randint(2, 3)
    n = random.randint(2, 3)
    k = utils.randex(-10, 10, [0])
    l = utils.randex(-10, 10, [0])
    A = sp.Matrix([[random.randint(-10, 10) for _ in range(m)] for _ in range(n)])
    B = sp.Matrix([[random.randint(-10, 10) for _ in range(m)] for _ in range(n)])
    C = k * A + l * B

    i = random.randint(1, m)
    j = random.randint(1, n)

    answer = C[i - 1, j - 1]
    return locals()
