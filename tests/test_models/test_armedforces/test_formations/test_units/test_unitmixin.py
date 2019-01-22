from models.armedforces.formations.units.unitmixin import UnitMixin
from models.configurations import SIMULATOR_CONFIG as CONFIG


class TestUnitMixin():

    def setup(self):
        print("setup")
        self.unit = UnitMixin()

    def test_init(self):
        print("test_init")
        assert self.unit.recharge >= 100 / CONFIG['speed_up_recharge_val'] and self.unit.recharge <= 1000 / CONFIG[
            'speed_up_recharge_val']

    def test_gmean(self):
        print('test_gmean')
        data_list = [1, 5, 9]
        assert self.unit.gmean(data_list) == 3.5568933044900626
        data_list = [23, 2, 16, 28, 3]
        assert self.unit.gmean(data_list) == 9.08304404352257
        data_list = [1, 4, 2, 6, 8, 12, 42, 51, 6]
        assert self.unit.gmean(data_list) == 7.304815360981009

    def test_check_unit_is_active(self):
        print('test_check_unit_is_active')
        self.unit.health = self.unit.health - 50
        assert self.unit.check_unit_is_active() is True
        self.unit.health = self.unit.health - 50
        assert self.unit.check_unit_is_active() is False
