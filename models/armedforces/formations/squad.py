from decimal import Decimal
from .formed import Formed
from .formationmixin import FormationMixin
from .formationfactory import FormationFactory


class Squad(FormationFactory, Formed, FormationMixin):

    def __init__(self):
        FormationMixin.__init__(self)
        self._attack_success = self.to_attack()

    """
    Formed(ABC) class realisation 
    ####################################################################################################################
    Begining:
    """

    def to_attack(self) -> Decimal:
        """
        Calculate the success rate of a squad’s attack.
        :return: (Decimal)
        """
        return round(Decimal(self.gmean([unit.to_attack() for unit in self._units])), 4)

    def to_damage(self) -> float:
        """
        Calculate the amount of damage caused by the squad to enemy
        :return: (float)
        """
        self._last_to_damage_val = sum([unit.to_damage() for unit in self._units])
        return self._last_to_damage_val

    def get_damage(self, dmg_val: float) -> None:
        """
        Get squad damage.
        :return: (None)
        """
        unit_dmg = dmg_val / len(self._units)
        for unit in self._units:
            unit.get_damage(unit_dmg)

    def incrs_unit_experience(self) -> None:
        """
        Increase the experience of each unit in squad.
        :return: (None)
        """
        for unit in self.units:
            unit.incrs_experience()

    """
    End
    ####################################################################################################################
    """
    """
    FormationFactory(ABC) class realisation 
    ####################################################################################################################
    Begining:
    """

    @classmethod
    def new_formation(cls):
        """
        Factory method.
        :return:
        """

        keys = [subclass.__qualname__ for subclass in FormationFactory.__subclasses__()]
        values = [subclass for subclass in FormationFactory.__subclasses__()]
        subclasses = dict(zip(keys, values))

        for key, value in subclasses.items():
            if cls.__qualname__ == key:
                return cls.__call__()

        return False

    """
    End
    ####################################################################################################################
    """
