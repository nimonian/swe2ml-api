import sympy as sp
import random
import src.utils as utils


def generate_vars():
    n = random.choice([2, 3])
    v = [random.randint(-10, 10) for _ in range(n)]
    _v = random.choice("uvwpqrab")
    l = sp.sqrt(sum(x**2 for x in v))
    u = [1 / l * x for x in v]
    u_approx = [x.evalf(5) for x in u]

    k = random.randrange(0, n)
    kth = ["first", "second", "third"][k]

    answer = str(u[k].evalf(3))

    return locals()
