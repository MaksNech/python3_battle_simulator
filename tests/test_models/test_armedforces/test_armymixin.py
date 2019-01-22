from models.armedforces.armymixin import ArmyMixin
from models.armedforces.formations.formed import Formed
from models.configurations import SIMULATOR_CONFIG as CONFIG


class TestArmyMixin():

    def setup(self):
        print("setup")
        self.armymixin_1 = ArmyMixin()
        self.armymixin_2 = ArmyMixin()
        self.all_armies_set = {self.armymixin_1, self.armymixin_2}

    def test_init(self):
        print("test_init")
        assert len(self.armymixin_1._own_formations) == CONFIG['formations_per_army']
        for formation in self.armymixin_2._own_formations:
            assert type(formation) in Formed.__subclasses__()

    def test_get_opposing_formations(self):
        print('test_get_opposing_formations')
        self.armymixin_1.get_opposing_formations(self.all_armies_set)
        self.armymixin_2.get_opposing_formations(self.all_armies_set)
        for op_formation in self.armymixin_1._opposing_formations:
            assert op_formation in self.armymixin_2._own_formations
        for op_formation in self.armymixin_2._opposing_formations:
            assert op_formation in self.armymixin_1._own_formations

    def test_sort_opposing_formations(self):
        print('test_sort_opposing_formations')
        self.armymixin_1.get_opposing_formations(self.all_armies_set)
        self.armymixin_2.get_opposing_formations(self.all_armies_set)
        self.armymixin_1.sort_opposing_formations()
        self.armymixin_2.sort_opposing_formations()
        for indx in range(len(self.armymixin_1._opposing_formations)):
            if indx == 1:
                assert self.armymixin_1._opposing_formations[indx]._attack_success >= \
                       self.armymixin_1._opposing_formations[indx - 1]._attack_success

    def test_check_army_is_active(self):
        print('test_check_army_is_active')
        assert self.armymixin_1.check_army_is_active() is True
        for own_formation in self.armymixin_1._own_formations:
            own_formation._active = False
        assert self.armymixin_1.check_army_is_active() is False
