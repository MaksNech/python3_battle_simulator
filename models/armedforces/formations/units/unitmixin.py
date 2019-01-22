import operator
from random import randint
from functools import reduce
from .timer import Timer
from models.configurations import SIMULATOR_CONFIG as CONFIG


class UnitMixin:

    def __init__(self):
        self._health = 100
        self._recharge = randint(100 / CONFIG['speed_up_recharge_val'], 1000 / CONFIG['speed_up_recharge_val'])
        self._active = True
        self._timer = Timer()
        self._last_attack_time = self._timer.get_current_time()

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @health.deleter
    def health(self):
        del self._health

    @property
    def recharge(self):
        return self._recharge

    @recharge.setter
    def recharge(self, value):
        self._recharge = value

    @recharge.deleter
    def recharge(self):
        del self._recharge

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value

    @active.deleter
    def active(self):
        del self._active

    @property
    def timer(self):
        return self._timer

    @timer.setter
    def timer(self, value):
        self._timer = value

    @timer.deleter
    def timer(self):
        del self._timer

    @property
    def last_attack_time(self):
        return self._last_attack_time

    @last_attack_time.setter
    def last_attack_time(self, value):
        self._last_attack_time = value

    @last_attack_time.deleter
    def last_attack_time(self):
        del self._last_attack_time

    def gmean(self, data_list: list) -> float:
        """
        Calculate the geometric mean.
        :param data_list: (list)
        :return: (float)
        """
        return reduce(operator.mul, data_list) ** (1/len(data_list))

    def check_unit_is_active(self) -> bool:
        """
        Check the unit activity.
        :return: (bool)
        """
        if self._active is True:
            if self._health > 0:
                self._active = True
                return True
            else:
                self._active = False
                return False
        else:
            return False
