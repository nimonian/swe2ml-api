import sympy as sp
import random
import src.utils as utils


def generate_vars():
    r = random.randint(2, 3)
    c = random.randint(2, 3)
    _M = random.choice("ABCDMNRST")
    _v = random.choice("uvwpqrabc")
    M = sp.Matrix([[random.randint(-10, 10) for _ in range(c)] for _ in range(r)])
    v = sp.Matrix([random.randint(-10, 10) for _ in range(c)])

    f = lambda r: " + ".join(f"{m} \\times {x}" for m, x in r)
    rows = [f(zip(r, v)) for r in (M.row(i) for i in range(M.rows))]

    Mv = M * v
    answer = sum(Mv.row(i)[0] for i in range(Mv.rows))
    return locals()
