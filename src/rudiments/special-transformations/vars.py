import sympy as sp
import random
import src.utils as utils
from functools import reduce


def generate_vars():
    case = random.choice([1, 2, 3])

    if case == 1:
        desc = "reflected in the $y$-axis"
        _R = R = sp.Matrix([[-1, 0], [0, 1]])

    if case == 2:
        desc = "reflected in the $x$-axis"
        _R = R = sp.Matrix([[1, 0], [0, -1]])

    if case == 3:
        t = random.randrange(1, 36)
        t *= 10
        desc = f"rotated by ${t}^\circ$"
        rad = lambda x: x / 360 * sp.pi

        _c, _s = sp.cos(t), sp.sin(t)
        _R = sp.Matrix([[_c, -_s], [_s, _c]])

        c, s = sp.cos(rad(t)), sp.sin(rad(t))
        R = sp.Matrix(
            [
                [utils.sig_figs(c, 3), utils.sig_figs(-s, 3)],
                [utils.sig_figs(s, 3), utils.sig_figs(c, 3)],
            ]
        )

    v = sp.Matrix([random.randint(-10, 10), random.randint(-10, 10)])
    w = R * v

    answer = reduce(lambda y, x: y * x, (w[i, 0] for i in range(w.rows)))

    if case == 3:
        answer = utils.sig_figs(answer, 3)

    return locals()
