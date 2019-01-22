from models.armedforces.army import Army


class TestArmy():

    def setup(self):
        print("setup")
        self.all_armies_set = {Army(), Army(), Army(), Army()}

    def test_random(self):
        print("test_random")
        for army in self.all_armies_set:
            isinstance(army.random(self.all_armies_set), Army)

    def test_weakest(self):
        print("test_weakest")
        for army in self.all_armies_set:
            weakest_op_formation = army.weakest(self.all_armies_set)
            for op_formation in army._opposing_formations:
                assert weakest_op_formation._attack_success <= op_formation._attack_success

    def test_strongest(self):
        print("test_strongest")
        for army in self.all_armies_set:
            strongest_op_formation = army.strongest(self.all_armies_set)
            for op_formation in army._opposing_formations:
                assert strongest_op_formation._attack_success >= op_formation._attack_success

    def test_new_army(self):
        print("test_new_army")
        assert isinstance(Army.new_army(), Army)
