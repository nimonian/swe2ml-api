import sympy as sp
import random
import src.utils as utils
from functools import reduce


def generate_vars():
    _u = random.choice("abcduvwpqrs")
    _v = random.choice([c for c in "abcduvwpqrs" if c != _u])
    n = random.choice([2, 3, 4])
    u = [random.randint(-10, 10) for _ in range(n)]
    v = [random.randint(-10, 10) for _ in range(n)]

    uv = [x * y for x, y in zip(u, v)]
    uu = [x * y for x, y in zip(u, u)]

    uv_str = str(uv[0]) + reduce(lambda x, y: x + utils.add_term(y), uv[1:], "")
    uu_str = str(uu[0]) + reduce(lambda x, y: x + utils.add_term(y), uu[1:], "")

    k = sp.Rational(sum(uv), sum(uu))

    uv_str = str(uv[0]) + reduce(lambda x, y: x + utils.add_term(y), uv[1:], "")
    uu_str = str(uv[0]) + reduce(lambda x, y: x + utils.add_term(y), uu[1:], "")

    proj_v = [k * x for x in u]
    answer = utils.sig_figs(utils.prod(proj_v), 3)

    return locals()
