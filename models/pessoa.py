# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class WelcomeElement:
    id: int
    nome: str
    cpf: None

    @staticmethod
    def from_dict(obj: Any) -> 'WelcomeElement':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        nome = from_str(obj.get("nome"))
        cpf = from_none(obj.get("cpf"))
        return WelcomeElement(id, nome, cpf)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["nome"] = from_str(self.nome)
        result["cpf"] = from_none(self.cpf)
        return result


def welcome_from_dict(s: Any) -> List[WelcomeElement]:
    return from_list(WelcomeElement.from_dict, s)


def welcome_to_dict(x: List[WelcomeElement]) -> Any:
    return from_list(lambda x: to_class(WelcomeElement, x), x)
