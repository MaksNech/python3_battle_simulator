from random import randint
from .unitary import Unitary
from .unitmixin import UnitMixin
from .unitfactory import UnitFactory


class Soldier(Unitary, UnitMixin, UnitFactory):

    def __init__(self):

        UnitMixin.__init__(self)
        self._experience = 0

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    @experience.deleter
    def experience(self):
        del self._experience

    """
    Unitary(ABC) class realisation 
    ####################################################################################################################
    Begining:
    """

    def to_attack(self) -> float:
        """
        Calculate the success rate of a soldier’s attack.
        :return: (float)
        """
        return 0.5 * (1 + self.health / 100) * randint(50 + self._experience, 100) / 100

    def to_damage(self) -> float:
        """
        Calculate the amount of damage caused by the soldier to enemy.
        :return: (float)
        """
        current_time = self._timer.get_current_time()

        if (current_time - self._last_attack_time) >= self._recharge:
            self._last_attack_time = current_time
            return 0.05 + self._experience / 100
        else:
            return float(0)

    def get_damage(self, dmg_val) -> None:
        """
        Get soldier damage.
        :return: (None)
        """
        if self._health > 0:
            self._health -= dmg_val

    def incrs_experience(self) -> None:
        """
        Increase the experience of a soldier.
        :return: (None)
        """
        if self._experience < 50:
            self._experience += 0.01

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
