from abc import ABC, abstractmethod


class Strategic(ABC):

    @abstractmethod
    def random(self, armies_set: set):
        pass

    @abstractmethod
    def weakest(self, armies_set: set):
        pass

    @abstractmethod
    def strongest(self, armies_set: set):
        pass
