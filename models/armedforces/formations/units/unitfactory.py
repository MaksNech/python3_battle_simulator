from abc import ABC, abstractmethod


class UnitFactory(ABC):

    @abstractmethod
    def new_unit(self):
        pass

