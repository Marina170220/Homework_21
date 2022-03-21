from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name: str, count: int):
        ...

    @abstractmethod
    def remove(self,  name: str, count: int):
        ...

    @abstractmethod
    def get_free_space(self):
        ...

    @abstractmethod
    def get_items(self):
        ...

    @abstractmethod
    def unique_items_count(self):
        ...
