from .armedforces.formations.units.soldier import Soldier
from .armedforces.formations.units.vehicle import Vehicle
from models.configurations import SIMULATOR_CONFIG as CONFIG


class BattleCustomLog():

    def display_armies_set(self, armies_set: set) -> None:
        """
        Display in terminal armies set.
        :param armies_set: (set)
        :return: (None)
        """
        if CONFIG['display_custom_log']:
            print('*' * 70)
            print('CURRENT ARMIES SET obj: {}'.format(armies_set))

    def display_army_info(self, army, step: int) -> int:
        """
        Display in terminal army info.
        :param army: (Army)
        :param step: (int)
        :return: (int)
        """
        if CONFIG['display_custom_log']:
            print('\n')
            print('#' * 70)
            print('STEP: {}'.format(step))
            print('#' * 70)
            print('\n')
            print('CURRENT ARMY obj: {}'.format(army))
            return step + 1

    def own_formation_info(self, own_formation) -> None:
        """
        Display in terminal own formation info.
        :param own_formation: Formed(abc) child class object
        :return: (None)
        """
        if CONFIG['display_custom_log']:
            print('*' * 70)
            print('CURRENT OWN_FORMATION obj: {}'.format(own_formation))
            print('contains:')
            for unit in own_formation._units:
                print(unit)

    def opposing_formation_info(self, opposing_formation) -> None:
        """
        Display in terminal opposing formation info.
        :param opposing_formation: Formed(abc) child class object
        :return: (None)
        """
        if CONFIG['display_custom_log']:
            print('*' * 70)
            print('CURRENT OPPOSING_FORMATION obj: {}'.format(opposing_formation))
            print('contains:')
            for unit in opposing_formation._units:
                print(unit)

    def units_recharging_info(self) -> None:
        """
        Display in terminal units recharging info
        :return: (None)
        """
        if CONFIG['display_custom_log']:
            print('*' * 70)
            print("UNITS ARE NOT READY, RECHARGING...")

    def successful_attack_info(self, own_formation, opposing_formation) -> None:
        """
        Display in terminal successful attack info.
        :param own_formation: Formed(abc) child class object
        :param opposing_formation: Formed(abc) child class object
        :return: (None)
        """
        if CONFIG['display_custom_log']:
            print('*' * 70)
            print('SUCCESSFULL ATTACK')
            print('CURRENT OWN_FORMATION attack success probability: {}'.format(own_formation._attack_success))
            print('CURRENT OWN_FORMATION damage value to opposing: {}'.format(own_formation._last_to_damage_val))
            print(
                'CURRENT OPPOSING_FORMATION attack success probability: {}'.format(opposing_formation._attack_success))
            print('CURRENT OPPOSING_FORMATION units health after attack:')
            for unit in opposing_formation._units:
                print('{}: {}'.format(unit, unit._health))

    def unsuccessful_attack_info(self, own_formation, opposing_formation) -> None:
        """
        Display in terminal unsuccessful attack info.
        :param own_formation: Formed(abc) child class object
        :param opposing_formation: Formed(abc) child class object
        :return: (None)
        """
        if CONFIG['display_custom_log']:
            print('*' * 70)
            print('UNSUCCESSFULL ATTACK')
            print('CURRENT OWN_FORMATION attack success probability: {}'.format(own_formation._attack_success))
            print(
                'CURRENT OPPOSING_FORMATION attack success probability: {}'.format(opposing_formation._attack_success))

    def unit_experience_info(self, own_formation) -> None:
        """
        Display in terminal unit experience info
        :param own_formation: Formed(abc) child class object
        :return: (None)
        """
        if CONFIG['display_custom_log']:
            print('*' * 70)
            print('CURRENT OWN_FORMATION units experience:')
            for unit in own_formation._units:
                if type(unit) is Soldier:
                    print('Soldier {}'.format(unit._experience))
                if type(unit) is Vehicle:
                    for op in unit._operators:
                        print('Operator of Vehicle {}'.format(op._experience))

    def destroyed_army_info(self, army) -> None:
        """
        Display in terminal destroyed army info
        :param army: (Army)
        :return: (None)
        """
        if CONFIG['display_custom_log']:
            print('*' * 70)
            print('DESTROYED ARMY obj: {}'.format(army))

    def winning_army_info(self, army) -> None:
        """
        Display in terminal winning army info
        :param army: (Army)
        :return: (None)
        """
        if CONFIG['display_custom_log']:
            print('\n')
            print('#' * 70)
            print()
            print('#' * 70)
            print('\n')
            print("—————————————————————————————————————")
            print("|     THE RESULTS OF THE BATTLE!    |")
            print("—————————————————————————————————————")
            print('THE WINNING ARMY obj: {}'.format(army))
            print('CONSIST OF:')
            for formation in army._own_formations:
                print('*' * 70)
                print('FORMATION obj: {}'.format(formation))
                print('contains:')
                for unit in formation._units:
                    if type(unit) is Soldier:
                        print('Soldier:')
                        print('{}\nhealth: {}\nexperience: {}'.format(unit, unit._health, unit._experience))
                    if type(unit) is Vehicle:
                        print('Vehicle:')
                        print('{}\nhealth: {}\noperators: {}'.format(unit, unit._health, unit._operators))
                        for op in unit._operators:
                            print('Operator of Vehicle:')
                            print('{}\nhealth: {}\nexperience: {}'.format(op, op._health, op._experience))
            print('#' * 70)
            print('SCROLL UP TO SEE RESULTS OF THE BATTLE')
