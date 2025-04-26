from jinja2 import Environment, FileSystemLoader
import sympy as sp
import src.utils as utils
import importlib


def generate(id: str):
    try:
        module = importlib.import_module(f"src.rudiments.{id}.vars")
        vars = module.generate_vars()
        env = Environment(loader=FileSystemLoader(f"src/rudiments/{id}"))

        problem = render_template(vars, env.get_template(f"problem.j2"))
        hint = render_template(vars, env.get_template(f"hint.j2"))
        solution = render_template(vars, env.get_template(f"solution.j2"))

        return problem, hint, solution, vars["answer"]
    except Exception as e:
        raise ValueError(f"Error creating Rudiment with id '{id}': {e}")


def render_template(vars, template):
    return template.render(**vars, sp=sp, utils=utils)
