from typing import TypeVar, Generic

_T_co = TypeVar("_T_co", covariant=True)


class Registry(Generic[_T_co]):
    def __init__(self):
        self.map: dict[str, _T_co] = {}

    def register(self, id: str, value: _T_co):
        if id in self.map:
            raise ValueError(f"ID {id} is already taken.")

        self.map[id] = value

    def unregister(self, id: str):
        del self.map[id]

    def get_id(self, registry_item: _T_co) -> str | None:
        for key, value in self.map.items():
            if value == registry_item:
                return key

        return None

    def from_id(self, id: str) -> _T_co | None:
        if id not in self.map:
            return None

        return self.map[id]
