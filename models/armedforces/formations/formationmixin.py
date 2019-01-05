from functools import reduce
from decimal import Decimal
from random import choice
from models.configurations import SIMULATOR_CONFIG as CONFIG
from .units.unitary import Unitary


class FormationMixin:

    def __init__(self):
        self._active = True
        self._units = [choice([subclass.__call__() for subclass in Unitary.__subclasses__()]) for i in
                       range(CONFIG['units_per_formation'])]
        self._attack_success = Decimal()
        self._last_to_damage_val = None

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value: float):
        self._active = value

    @active.deleter
    def active(self):
        del self._active

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, value: float):
        self._units = value

    @units.deleter
    def units(self):
        del self._units

    @property
    def attack_success(self):
        return self._attack_success

    @attack_success.setter
    def attack_success(self, value: float):
        self._attack_success = value

    @attack_success.deleter
    def attack_success(self):
        del self._attack_success

    @property
    def last_to_damage_val(self):
        return self._last_to_damage_val

    @last_to_damage_val.setter
    def last_to_damage_val(self, value: float):
        self._last_to_damage_val = value

    @last_to_damage_val.deleter
    def last_to_damage_val(self):
        del self._last_to_damage_val

    def gmean(self, data_list: list) -> float:
        """
        Сalculate the geometric mean.
        :param data_list: (list)
        :return: (float)
        """
        return reduce(lambda x, y: x * y, data_list) ** (1.0 / len(data_list))

    def check_formation_is_active(self) -> bool:
        """
        Check the formation activity.
        :return: (bool)
        """
        if self._active is True:
            for unit in self._units:
                if unit.check_unit_is_active() is False:
                    self._units.remove(unit)
            if len(self._units) > 0:
                self._active = True
                return True
            else:
                self._active = False
                return False
