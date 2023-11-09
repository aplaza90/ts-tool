from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def execute(self):
        pass
