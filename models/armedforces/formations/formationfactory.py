from abc import ABC, abstractmethod


class FormationFactory(ABC):

    @abstractmethod
    def new_formation(self):
        pass
