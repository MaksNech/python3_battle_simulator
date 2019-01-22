from random import randint
from .unitary import Unitary
from .unitmixin import UnitMixin
from .soldier import Soldier
from .unitfactory import UnitFactory
from models.configurations import SIMULATOR_CONFIG as CONFIG


class Vehicle(Unitary, UnitMixin, UnitFactory):

    def __init__(self):
        UnitMixin.__init__(self)
        self._recharge = randint(1000 / CONFIG['speed_up_recharge_val'], 2000 / CONFIG['speed_up_recharge_val'])
        self._operators = [Soldier() for i in range(randint(1, 3))]

    @property
    def operators(self):
        return self._operators

    @operators.setter
    def operators(self, value: list):
        self._operators = value

    @operators.deleter
    def operators(self):
        del self._operators

    def get_operators_attack_val(self) -> list:
        """
        Get a list of the success rate of a operator’s attack values.
        :return: (list)
        """

        return [operator.to_attack() for operator in self.operators]

    def calc_operator_dmg(self, dmg_val: float, operator_index: int, percentage: int) -> None:
        """
        Get operator damage.
        :param dmg_val: (float)
        :param operator_index: (int)
        :param percentage: (int)
        :return: (None)
        """
        if self._operators[operator_index].health > 0:
            self._operators[operator_index].health = self._operators[operator_index].health - (
                    (dmg_val / 100) * percentage)

    """
    Unitary(ABC) class realisation 
    ####################################################################################################################
    Begining:
    """

    def to_attack(self) -> float:
        """
        Calculate the success rate of a vehicle’s attack.
        :return: (float)
        """

        return 0.5 * (1 + self.health / 100) * self.gmean(self.get_operators_attack_val())

    def to_damage(self) -> float:
        """
        Calculate the amount of damage caused by the vehicle to enemy.
        :return: (float)
        """

        current_time = self._timer.get_current_time()

        if (current_time - self._last_attack_time) >= self._recharge:
            self._last_attack_time = current_time
            return 0.1 + (sum([operator._experience for operator in self._operators]) / 100)
        else:
            return 0

    def get_damage(self, dmg_val: float) -> None:
        """
        Get vehicle damage.
        :param dmg_val: (float)
        :return: (None)
        """

        for operator in self._operators:
            if operator._health <= 0:
                self._operators.remove(operator)

        if len(self._operators) == 3:
            self.calc_operator_dmg(dmg_val, 0, 20)
            self.calc_operator_dmg(dmg_val, 1, 10)
            self.calc_operator_dmg(dmg_val, 2, 10)
        elif len(self._operators) == 2:
            self.calc_operator_dmg(dmg_val, 0, 20)
            self.calc_operator_dmg(dmg_val, 1, 20)
        elif len(self._operators) == 1:
            self.calc_operator_dmg(dmg_val, 0, 40)

        self._operators = [operator for operator in self._operators if operator._health > 0]

        health_list = ([operator.health for operator in self._operators])
        if len(self._operators) > 0:
            health_list.append(self._health - ((dmg_val / 100) * 60))
            self._health = sum(health_list) / len(health_list)

        else:
            self._health = -1

    def incrs_experience(self) -> None:
        """
        Increase the experience of a vehicle.
        :return: (None)
        """
        for operator in self._operators:
            if operator._experience < 50:
                operator._experience += 0.01

    """
    End
    ####################################################################################################################
    """

    """
    UnitFactory(ABC) class realisation 
    ####################################################################################################################
    Begining:
    """

    @classmethod
    def new_unit(cls):
        """
        Factory method.
        :return:
        """

        keys = [subclass.__qualname__ for subclass in UnitFactory.__subclasses__()]
        values = [subclass for subclass in UnitFactory.__subclasses__()]
        subclasses = dict(zip(keys, values))

        for key, value in subclasses.items():
            if cls.__qualname__ == key:
                return cls.__call__()

        return False

    """
    End
    ####################################################################################################################
    """
