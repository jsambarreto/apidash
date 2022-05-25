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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Series:
    serie: str
    cursando: int
    capacidade: int
    vagas: int

    @staticmethod
    def from_dict(obj: Any) -> 'Series':
        assert isinstance(obj, dict)
        serie = from_str(obj.get("SERIE"))
        cursando = from_int(obj.get("CURSANDO"))
        capacidade = from_int(obj.get("CAPACIDADE"))
        vagas = from_int(obj.get("VAGAS"))
        return Series(serie, cursando, capacidade, vagas)

    def to_dict(self) -> dict:
        result: dict = {}
        result["SERIE"] = from_str(self.serie)
        result["CURSANDO"] = from_int(self.cursando)
        result["CAPACIDADE"] = from_int(self.capacidade)
        result["VAGAS"] = from_int(self.vagas)
        return result


@dataclass
class Escola:
    id_escola: int
    series: List[Series]
    escola_resumido: str
    escola_completo: str
    diretor: str
    telefone: str
    latitude: str
    longitude: str
    endereco: str
    email: str

    @staticmethod
    def from_dict(obj: Any) -> 'Escola':
        assert isinstance(obj, dict)
        id_escola = from_int(float(obj.get("ID_ESCOLA")))
        series = from_list(Series.from_dict, obj.get("SERIES"))
        escola_resumido = from_str(obj.get("ESCOLA_RESUMIDO"))
        escola_completo = from_str(obj.get("ESCOLA_COMPLETO"))
        diretor = from_str(obj.get("DIRETOR"))
        telefone = from_str(obj.get("TELEFONE"))
        latitude = from_str(obj.get("LATITUDE"))
        longitude = from_str(obj.get("LONGITUDE"))
        endereco = from_str(obj.get("ENDERECO"))
        email = from_str(obj.get("EMAIL"))
        return Escola(id_escola, series, escola_resumido, escola_completo, diretor, telefone, latitude, longitude, endereco, email)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ID_ESCOLA"] = from_int(float(self.id_escola))
        result["SERIES"] = from_list(lambda x: to_class(Series, x), self.series)
        result["ESCOLA_RESUMIDO"] = from_str(self.escola_resumido)
        result["ESCOLA_COMPLETO"] = from_str(self.escola_completo)
        result["DIRETOR"] = from_str(self.diretor)
        result["TELEFONE"] = from_str(self.telefone)
        result["LATITUDE"] = from_str(self.latitude)
        result["LONGITUDE"] = from_str(self.longitude)
        result["ENDERECO"] = from_str(self.endereco)
        result["EMAIL"] = from_str(self.email)
        return result


def welcome_from_dict(s: Any) -> List[Escola]:
    return from_list(Escola.from_dict, s)


def welcome_to_dict(x: List[Escola]) -> Any:
    return from_list(lambda x: to_class(Escola, x), x)
