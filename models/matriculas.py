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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class WelcomeElement:
    id_escola: int
    escola: str
    zona: str
    ano: str
    g1: int
    g2: int
    g3: int
    g4: int
    g5: int
    a1: int
    a2: int
    a3: int
    a4: int
    a5: int
    a6: int
    a7: int
    a8: int
    a9: int
    ejai: int
    ejaii: int
    ejaiii: int
    ejaiv: int
    ejav: int
    mei: int
    mf9: int
    mej: int
    cf: int
    total: int

    @staticmethod
    def from_dict(obj: Any) -> 'WelcomeElement':
        assert isinstance(obj, dict)
        id_escola = from_int(obj.get("Id_escola"))
        escola = from_str(obj.get("Escola"))
        zona = from_str(obj.get("Zona"))
        ano = from_str(obj.get("Ano"))
        g1 = from_int(obj.get("G1"))
        g2 = from_int(obj.get("G2"))
        g3 = from_int(obj.get("G3"))
        g4 = from_int(obj.get("G4"))
        g5 = from_int(obj.get("G5"))
        a1 = from_int(obj.get("A1"))
        a2 = from_int(obj.get("A2"))
        a3 = from_int(obj.get("A3"))
        a4 = from_int(obj.get("A4"))
        a5 = from_int(obj.get("A5"))
        a6 = from_int(obj.get("A6"))
        a7 = from_int(obj.get("A7"))
        a8 = from_int(obj.get("A8"))
        a9 = from_int(obj.get("A9"))
        ejai = from_int(obj.get("EJAI"))
        ejaii = from_int(obj.get("EJAII"))
        ejaiii = from_int(obj.get("EJAIII"))
        ejaiv = from_int(obj.get("EJAIV"))
        ejav = from_int(obj.get("EJAV"))
        mei = from_int(obj.get("MEI"))
        mf9 = from_int(obj.get("MF9"))
        mej = from_int(obj.get("MEJ"))
        cf = from_int(obj.get("CF"))
        total = from_int(obj.get("Total"))
        return WelcomeElement(id_escola, escola, zona, ano, g1, g2, g3, g4, g5, a1, a2, a3, a4, a5, a6, a7, a8, a9, ejai, ejaii, ejaiii, ejaiv, ejav, mei, mf9, mej, cf, total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id_escola"] = from_int(self.id_escola)
        result["Escola"] = from_str(self.escola)
        result["Zona"] = from_str(self.zona)
        result["Ano"] = from_str(self.ano)
        result["G1"] = from_int(self.g1)
        result["G2"] = from_int(self.g2)
        result["G3"] = from_int(self.g3)
        result["G4"] = from_int(self.g4)
        result["G5"] = from_int(self.g5)
        result["A1"] = from_int(self.a1)
        result["A2"] = from_int(self.a2)
        result["A3"] = from_int(self.a3)
        result["A4"] = from_int(self.a4)
        result["A5"] = from_int(self.a5)
        result["A6"] = from_int(self.a6)
        result["A7"] = from_int(self.a7)
        result["A8"] = from_int(self.a8)
        result["A9"] = from_int(self.a9)
        result["EJAI"] = from_int(self.ejai)
        result["EJAII"] = from_int(self.ejaii)
        result["EJAIII"] = from_int(self.ejaiii)
        result["EJAIV"] = from_int(self.ejaiv)
        result["EJAV"] = from_int(self.ejav)
        result["MEI"] = from_int(self.mei)
        result["MF9"] = from_int(self.mf9)
        result["MEJ"] = from_int(self.mej)
        result["CF"] = from_int(self.cf)
        result["Total"] = from_int(self.total)
        return result


def welcome_from_dict(s: Any) -> List[WelcomeElement]:
    return from_list(WelcomeElement.from_dict, s)


def welcome_to_dict(x: List[WelcomeElement]) -> Any:
    return from_list(lambda x: to_class(WelcomeElement, x), x)
