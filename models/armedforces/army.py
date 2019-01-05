from random import choice
from .armymixin import ArmyMixin
from .strategic import Strategic
from .armyfactory import ArmyFactory


class Army(ArmyFactory, Strategic, ArmyMixin):

    def __init__(self):
        ArmyMixin.__init__(self)

    """
    Strategic(ABC) class realisation 
    ####################################################################################################################
    Begining:
    """

    def random(self, all_armies_set: set):
        """
        Choose opposing formation by random.
        :param all_armies_set: (set)
        :return: any Formed(abc) child class object
        """
        self.get_opposing_formations(all_armies_set)
        return choice(self._opposing_formations)

    def weakest(self, all_armies_set: set):
        """
        Choose the weakest opposing formation.
        :param all_armies_set: (set)
        :return: the weakest Formed(abc) child class object
        """
        self.get_opposing_formations(all_armies_set)
        return self._opposing_formations[0]

    def strongest(self, all_armies_set: set):
        """
        Choose the strongest opposing formation.
        :param all_armies_set: (set)
        :return: the strongest Formed(abc) child class object
        """
        self.get_opposing_formations(all_armies_set)
        return self._opposing_formations[len(self._opposing_formations) - 1]

    """
    End
    ####################################################################################################################
    """
    """
    ArmyFactory(ABC) class realisation 
    ####################################################################################################################
    Begining:
    """

    @classmethod
    def new_army(cls):
        """
        Factory method.
        :return:
        """

        keys = [subclass.__qualname__ for subclass in ArmyFactory.__subclasses__()]
        values = [subclass for subclass in ArmyFactory.__subclasses__()]
        subclasses = dict(zip(keys, values))

        for key, value in subclasses.items():
            if cls.__qualname__ == key:
                return cls.__call__()

        return False

    """
    End
    ####################################################################################################################
    """
