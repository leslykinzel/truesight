from typing import Iterable, Mapping, Optional


class GQL:

    def __init__(
            self,
            name: str,
            args: Optional[Mapping[str, object]] = None,
            fields: Optional[Iterable['GQL']] = None
        ):
        self.name = name
        self.args = args or {}
        self.fields = fields or {}

    def render(self, indent: int = 0) -> str:
        pad = " " * indent
        args = ""
        if self.args:
            args = "(" + ", ".join(f"{k}: {v}" for k, v in self.args.items()) + ")"
        if not self.fields:
            return f"{pad}{self.name}{args}"
        inner = "\n".join(f.render(indent + 1) for f in self.fields)
        return f"""{pad}{self.name}{args}{{\n{inner}\n{pad}}}"""


class Query:
    """ Wraps GQL fields into query string.
    """

    def __init__(self, *fields: GQL):
        self.fields = fields

    def render(self) -> str:
        inner = "\n".join(f.render(1) for f in self.fields)
        return "{\n" + inner + "\n}"
