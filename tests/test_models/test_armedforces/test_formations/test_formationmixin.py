from models.armedforces.formations.formationmixin import FormationMixin
from models.configurations import SIMULATOR_CONFIG as CONFIG
from models.armedforces.formations.units.unitary import Unitary
from models.armedforces.formations.units.soldier import Soldier
from models.armedforces.formations.units.vehicle import Vehicle


class TestFormationMixin():

    def setup(self):
        print("setup")
        self.formation = FormationMixin()

    def test_init(self):
        print("test_init")
        assert len(self.formation._units) == CONFIG['units_per_formation']
        for unit in self.formation._units:
            assert type(unit) in Unitary.__subclasses__()

    def test_gmean(self):
        print('test_gmean')
        data_list = [1, 5, 9]
        assert self.formation.gmean(data_list) == 3.5568933044900626
        data_list = [23, 2, 16, 28, 3]
        assert self.formation.gmean(data_list) == 9.08304404352257
        data_list = [1, 4, 2, 6, 8, 12, 42, 51, 6]
        assert self.formation.gmean(data_list) == 7.304815360981009

    def test_check_formation_is_active(self):
        print('test_check_formation_is_active')
        self.formation._units = [Soldier(), Vehicle(), Soldier(), Soldier(), Vehicle()]
        self.formation._units[0]._active = False
        self.formation._units[1]._active = False
        assert self.formation.check_formation_is_active() is True
        self.formation._units[0]._active = False
        self.formation._units[1]._active = False
        self.formation._units[2]._active = False
        assert self.formation.check_formation_is_active() is False
