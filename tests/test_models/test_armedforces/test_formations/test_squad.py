from decimal import Decimal
from models.armedforces.formations.squad import Squad
from models.armedforces.formations.units.soldier import Soldier


class TestSquad():

    def setup(self):
        print("setup")
        self.squad = Squad()

    def test_to_attack(self):
        print("test_to_attack")
        assert isinstance(self.squad.to_attack(), Decimal)
        assert self.squad.to_attack() > 0

    def test_to_damage(self):
        print("test_to_damage")
        self.squad._units = [Soldier(), Soldier(), Soldier(), Soldier(), Soldier()]
        self.squad._units[0]._experience = 10
        self.squad._units[0]._last_attack_time = self.squad._units[0]._last_attack_time - self.squad._units[0]._recharge
        self.squad._units[1]._experience = 14
        self.squad._units[1]._last_attack_time = self.squad._units[1]._last_attack_time - self.squad._units[1]._recharge
        self.squad._units[2]._experience = 8
        self.squad._units[2]._last_attack_time = self.squad._units[2]._last_attack_time - self.squad._units[2]._recharge
        self.squad._units[3]._experience = 12
        self.squad._units[3]._last_attack_time = self.squad._units[3]._last_attack_time - self.squad._units[3]._recharge
        self.squad._units[4]._experience = 9
        self.squad._units[4]._last_attack_time = self.squad._units[4]._last_attack_time - self.squad._units[4]._recharge
        assert self.squad.to_damage() == 0.78
        self.squad._units = [Soldier(), Soldier(), Soldier()]
        self.squad._units[0]._experience = 40.5
        self.squad._units[0]._last_attack_time = self.squad._units[0]._last_attack_time - self.squad._units[0]._recharge
        self.squad._units[1]._experience = 12
        self.squad._units[1]._last_attack_time = self.squad._units[1]._last_attack_time - self.squad._units[1]._recharge
        self.squad._units[2]._experience = 45
        self.squad._units[2]._last_attack_time = self.squad._units[2]._last_attack_time - self.squad._units[2]._recharge
        assert self.squad.to_damage() == 1.125

    def test_get_damage(self):
        print("test_get_damage")
        self.squad._units = [Soldier(), Soldier(), Soldier()]
        self.squad.get_damage(12.6)
        for unit in self.squad._units:
            assert unit._health == 95.8
        self.squad.get_damage(21)
        for unit in self.squad._units:
            assert unit._health == 88.8

    def test_incrs_experience(self):
        print("test_incrs_experience")
        self.squad._units = [Soldier(), Soldier(), Soldier()]
        self.squad._units[0]._experience = 4.8
        self.squad._units[1]._experience = 9.5
        self.squad._units[2]._experience = 12.64
        self.squad.incrs_unit_experience()
        assert self.squad._units[0]._experience == 4.81
        assert self.squad._units[1]._experience == 9.51
        assert self.squad._units[2]._experience == 12.65

    def test_new_formation(self):
        print("test_new_formation")
        assert isinstance(Squad.new_formation(), Squad)
