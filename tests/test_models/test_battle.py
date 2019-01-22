import mock
from models.configurations import SIMULATOR_CONFIG as CONFIG
from models.battle import Battle
from models.armedforces.army import Army


class TestBattle():

    def setup(self):
        print('setup')
        self.battle = Battle()
        self.strategy_list = ['random', 'weakest', 'strongest']
        self.speed_up_recharge_list = [1, 10, 100]

    def test_select_armies_creation_way(self):
        print('test_select_armies_creation_way')
        with mock.patch('builtins.input', return_value=0):
            self.battle.select_armies_creation_way()
            assert CONFIG['armies_creation_way'] == 0 or CONFIG['armies_creation_way'] == 1

    def test_set_simulator_config(self):
        print('test_set_simulator_config')

        with mock.patch('builtins.input', return_value=2):
            self.battle.set_armies_amount_config()
            assert CONFIG['armies_amount'] >= 2

        with mock.patch('builtins.input', return_value=0):
            self.battle.set_attack_strategy_config(self.strategy_list)
            assert CONFIG['attack_strategy'] in self.strategy_list

        with mock.patch('builtins.input', return_value=2):
            self.battle.set_speed_up_recharge_val_config(self.speed_up_recharge_list)
            assert CONFIG['speed_up_recharge_val'] in self.speed_up_recharge_list

        with mock.patch('builtins.input', return_value=5):
            self.battle.set_formations_per_army_config()
            assert CONFIG['formations_per_army'] >= 2

        with mock.patch('builtins.input', return_value=10):
            self.battle.set_units_per_formation_config()
            assert CONFIG['units_per_formation'] >= 5 and CONFIG['units_per_formation'] <= 10

        with mock.patch('builtins.input', return_value=0):
            self.battle.set_enable_python_logging_config()
            assert CONFIG['enable_python_logging'] == 0 or CONFIG['enable_python_logging'] == 1

        with mock.patch('builtins.input', return_value=0):
            self.battle.set_display_custom_log_config()
            assert CONFIG['display_custom_log'] == 0 or CONFIG['display_custom_log'] == 1

    def test_create_armies(self):
        print('test_create_armies')
        self.battle.create_armies()
        assert len(self.battle._armies_set) == CONFIG['armies_amount']
        for army in self.battle._armies_set:
            assert isinstance(army, Army)

    def test_check_battle_is_over(self):
        print('test_check_battle_is_over')
        self.battle._armies_set = {Army(), Army()}
        assert self.battle.check_battle_is_over() is True
        self.battle._armies_set = {Army()}
        assert self.battle.check_battle_is_over() is False
