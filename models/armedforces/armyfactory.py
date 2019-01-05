from abc import ABC, abstractmethod


class ArmyFactory(ABC):

    @abstractmethod
    def new_army(self):
        pass
