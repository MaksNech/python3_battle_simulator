from abc import ABC, abstractmethod


class Formed(ABC):

    @abstractmethod
    def to_attack(self):
        pass

    @abstractmethod
    def to_damage(self):
        pass

    @abstractmethod
    def get_damage(self, dmg_val: float):
        pass

    @abstractmethod
    def incrs_unit_experience(self):
        pass
