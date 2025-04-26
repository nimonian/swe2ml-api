from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel, Field, computed_field
import sympy as sp
import src.utils as u
import importlib


class Rudiment(BaseModel):
    id: str
    answer: int | float
    args: dict = Field(exclude=True)
    env: Environment = Field(exclude=True)

    class Config:
        arbitrary_types_allowed = True

    @computed_field
    def problem(self) -> str:
        return self.render_template("problem")

    @computed_field
    def hint(self) -> str:
        return self.render_template("hint")

    @computed_field
    def solution(self) -> str:
        return self.render_template("solution")

    def render_template(self, name: str) -> str:
        template = self.env.get_template(f"{name}.j2")
        return template.render(**self.args, sp=sp, utils=u)

    @classmethod
    def create(cls, id: str):
        try:
            mod = importlib.import_module(f"src.rudiments.{id}.vars")
            args = mod.generate_vars()
            env = Environment(loader=FileSystemLoader(f"src/rudiments/{id}"))
            return cls(id=id, args=args, answer=args["answer"], env=env)
        except Exception as e:
            raise ValueError(f"Error creating Rudiment with id '{id}': {e}")
