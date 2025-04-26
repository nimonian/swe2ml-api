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
    dot = sum(uv)

    u_sq_sum = sum(x**2 for x in u)
    u_sq_sum_list = " + ".join(f"{utils.brackets_if_negative(x)}^2" for x in u)

    v_sq_sum = sum(x**2 for x in v)
    v_sq_sum_list = " + ".join(f"{utils.brackets_if_negative(x)}^2" for x in v)

    exact = dot / (sp.sqrt(u_sq_sum) * sp.sqrt(v_sq_sum))
    answer = str(exact.evalf(3))

    return locals()
