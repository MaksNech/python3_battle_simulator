from random import choice
from models.configurations import SIMULATOR_CONFIG as CONFIG
from .formations.formed import Formed


class ArmyMixin:

    def __init__(self):
        self._own_formations = [choice([subclass.__call__() for subclass in Formed.__subclasses__()]) for i in
                                range(CONFIG['formations_per_army'])]
        self._opposing_formations = []
        self._destroyed_own_formations = []
        self._active = True

    @property
    def own_formations(self):
        return self._own_formations

    @own_formations.setter
    def own_formations(self, value: list):
        self._own_formations = value

    @own_formations.deleter
    def own_formations(self):
        del self._own_formations

    @property
    def opposing_formations(self):
        return self._opposing_formations

    @opposing_formations.setter
    def opposing_formations(self, value: list):
        self._opposing_formations = value

    @opposing_formations.deleter
    def opposing_formations(self):
        del self._opposing_formations

    @property
    def destroyed_own_formations(self):
        return self._destroyed_own_formations

    @destroyed_own_formations.setter
    def destroyed_own_formations(self, value: list):
        self._destroyed_own_formations = value

    @destroyed_own_formations.deleter
    def destroyed_own_formations(self):
        del self._destroyed_own_formations

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value: bool):
        self._active = value

    @active.deleter
    def active(self):
        del self._active

    def get_opposing_formations(self, all_armies_set: set) -> None:
        """
        Calculate and get enemy formations.
        :param all_armies_set: (set)
        :return: (None)
        """
        opposing_formations = []
        for army in {self}.symmetric_difference(all_armies_set):
            for formation in army._own_formations:
                opposing_formations.append(formation)

        self._opposing_formations = opposing_formations
        self.sort_opposing_formations()

    def sort_opposing_formations(self) -> None:
        """
        Sort enemy formations.
        :return: (None)
        """

        self._opposing_formations.sort(key=lambda x: x._attack_success, reverse=False)

    def check_army_is_active(self) -> bool:
        """
        Check the army activity.
        :return: (bool)
        """
        if self._active is True:
            for own_formation in self._own_formations:
                if own_formation.check_formation_is_active():
                    continue
                else:
                    self._own_formations.remove(own_formation)

            if len(self._own_formations) > 0:
                self._active = True
                return True
            else:
                self._active = False
                return False
