import datetime
from .log import BattleLog
from .jsonparser import JsonParser
from .configurations import SIMULATOR_CONFIG as CONFIG
from .armedforces.army import Army


class Battle(BattleLog, JsonParser):

    def __init__(self):
        self._armies_set = set()
        self._step = 1

    @property
    def armies_set(self):
        return self._armies_set

    @armies_set.setter
    def armies_set(self, value):
        self._armies_set = value

    @armies_set.deleter
    def armies_set(self):
        del self._armies_set

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value

    @step.deleter
    def step(self):
        del self._step

    def show_greetings(self) -> None:
        """
        Show greetings.
        :return: (None)
        """
        print("————————————————————————————————————")
        print("| Welcome to the battle simulator! |")
        print("————————————————————————————————————")

    def show_description(self) -> None:
        """
        Show simulator description.
        :return: (None)
        """
        print("——————————————————————————————————————")
        print("|This simulator should determine the |\n"
              "|outcome of the battle,based on      |\n"
              "|probabilistic calculations.         |")
        print("|After launching the simulator, all  |\n"
              "|units of the armies will attack each|\n"
              "|other until only one army remains.  |")
        print("——————————————————————————————————————")

    def set_simulator_config(self) -> None:
        """
        Setting simulator configurations.
        :return: (None)
        """
        strategy_list = ['random', 'weakest', 'strongest']
        speed_up_recharge_list = [1, 10, 100]
        print('*' * 46)
        while True:
            try:
                CONFIG['armies_amount'] = int(input('Enter the number of armies (from 2 or more): '))
                if CONFIG['armies_amount'] < 2:
                    raise ValueError
                break
            except ValueError:
                print("Invalid integer. The number must be in the range from 2 or more.")
        print('*' * 46)
        while True:
            try:
                value = int(input(
                    '''Choose attack strategy per army:
                    "random":    input 0
                    "weakest":   input 1
                    "strongest": input 2
                    : '''))
                if value < 0 or value > 2:
                    raise ValueError
                CONFIG['attack_strategy'] = strategy_list[value]
                break
            except ValueError:
                print("Invalid integer. The number must be in the range of 0-2.")
        print('*' * 46)
        while True:
            try:
                value = int(input(
                    '''Choose speed-up for recharge:
                    "zero":       input 0
                    "decimal":    input 1
                    "centesimal": input 2
                    : '''))
                if value < 0 or value > 2:
                    raise ValueError
                CONFIG['speed_up_recharge_val'] = speed_up_recharge_list[value]
                break
            except ValueError:
                print("Invalid integer. The number must be in the range of 0-2.")
        print('*' * 55)
        while True:
            try:
                CONFIG['formations_per_army'] = int(input('Enter the number of formations per army (from 2 or more): '))
                if CONFIG['formations_per_army'] < 2:
                    raise ValueError
                break
            except ValueError:
                print("Invalid integer. The number must be in the range from 2 or more.")

        print('*' * 55)
        while True:
            try:
                CONFIG['units_per_formation'] = int(input('Enter the number of units per formation (from 5 to 10): '))
                if CONFIG['units_per_formation'] < 5 or CONFIG['units_per_formation'] > 10:
                    raise ValueError
                break
            except ValueError:
                print("Invalid integer. The number must be in the range of 5-10.")

        print('*' * 55)
        while True:
            try:
                CONFIG['display_log'] = int(
                    input('Display battle logs in terminal? ("Yes" — input 1 | "No" — input 0): '))
                if CONFIG['display_log'] < 0 or CONFIG['display_log'] > 1:
                    raise ValueError
                break
            except ValueError:
                print("Invalid integer. The number must be 0 or 1.")
        print('*' * 55)

    def select_armies_creation_way(self) -> None:
        """
        Choosing way how to create armies.
        :return: (None)
        """
        while True:
            try:
                CONFIG['armies_creation_way'] = int(input(
                    '''Choose way how to create armies:
                       "by setting configurations"   input 1 
                       "by loading JSON file"        input 0
                       : '''))
                if CONFIG['armies_creation_way'] < 0 or CONFIG['armies_creation_way'] > 1:
                    raise ValueError
                break
            except ValueError:
                print("Invalid integer. The number must be 0 or 1.")

        if (CONFIG['armies_creation_way']):
            self.set_simulator_config()
            self.create_armies()
        else:
            jsonparser = JsonParser()
            self._armies_set = (jsonparser.json_parse(CONFIG['json_armies_path']))

    def show_battle_result(self, armies_set: set, battle_timedelta) -> None:
        """
        Show battle results.
        :param armies_set: (set)
        :param battle_timedelta: (datetime.timedelta)
        :return: (None)
        """
        print("—————————————————————————————————————")
        print("|       The battle is over!         |")
        print("|     BATTLE TIME: mm:{} ss:{}       |".format(battle_timedelta.seconds // 60, battle_timedelta.seconds))
        print("—————————————————————————————————————")
        print('The winning army is: {}'.format(armies_set))

    def create_armies(self) -> set:
        """
        Creating armies.
        :return: (set)
        """
        armies_set = set()
        for i in range(CONFIG['armies_amount']):
            armies_set.add(Army())
        self._armies_set = armies_set
        print('A set of armies ready for the battle:\n {}'.format(self._armies_set))
        return armies_set

    def check_battle_is_over(self) -> bool:
        """
        Check if the battle is over.
        :return: (bool)
        """
        if len(self._armies_set) > 1:
            return True
        else:
            return False

    def run_battle_cycle(self) -> None:
        """
        Starts battle cycles.
        :return: (None)
        """
        print("The battle is running, please wait...")
        start_time = datetime.datetime.now()
        lock = True
        while (lock):
            self.display_armies_set(self._armies_set)

            for army in self._armies_set:
                self._step = self.display_army_info(army, self._step)

                for own_formation in army.own_formations:
                    self.own_formation_info(own_formation)
                    strategy = army.__getattribute__(CONFIG['attack_strategy'])
                    opposing_formation = strategy(self._armies_set)
                    self.opposing_formation_info(opposing_formation)

                    if own_formation._attack_success > opposing_formation._attack_success:
                        dmg_val_to_opposing = own_formation.to_damage()
                        if dmg_val_to_opposing > 0:
                            opposing_formation.get_damage(dmg_val_to_opposing)
                            self.successful_attack_info(own_formation, opposing_formation)
                            own_formation.incrs_unit_experience()
                            self.unit_experience_info(own_formation)
                        else:
                            self.units_recharging_info()

                    else:
                        self.unsuccessful_attack_info(own_formation, opposing_formation)

                if army.check_army_is_active() is False:
                    self.destroyed_army_info(army)
                    self._armies_set.remove(army)
                    lock = self.check_battle_is_over()
                    break

        end_time = datetime.datetime.now()
        battle_timedelta = end_time - start_time
        self.show_battle_result(self._armies_set, battle_timedelta)

        for army in self._armies_set:
            self.winning_army_info(army)

    def start(self) -> None:
        """
        Battle main method.
        :return: (None)
        """
        self.show_greetings()
        self.show_description()
        self.select_armies_creation_way()
        self.run_battle_cycle()
