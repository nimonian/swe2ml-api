import sympy as sp
import random
import src.utils as utils
from functools import reduce


def generate_vars():
    n = random.choice([2, 3])
    u = [random.randint(-10, 10) for _ in range(n)]
    v = [random.randint(-10, 10) for _ in range(n)]
    uv = [x * y for x, y in zip(u, v)]
    uv_str = str(uv[0]) + reduce(lambda x, y: x + utils.add_term(y), uv[1:], "")
    answer = sum(uv)

    return locals()
