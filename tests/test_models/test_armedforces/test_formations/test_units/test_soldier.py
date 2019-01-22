from models.armedforces.formations.units.soldier import Soldier


class TestSoldier():

    def setup(self):
        print("setup")
        self.soldier = Soldier()

    def test_to_attack(self):
        print("test_to_attack")
        assert isinstance(self.soldier.to_attack(), float)
        assert self.soldier.to_attack() > 0

    def test_to_damage(self):
        print("test_to_damage")
        self.soldier.last_attack_time=self.soldier._timer.get_current_time()
        self.soldier.last_attack_time -= self.soldier.recharge
        self.soldier.experience = 7
        assert self.soldier.to_damage() == 0.12000000000000001
        self.soldier.last_attack_time -= self.soldier.recharge
        self.soldier.experience = 25
        assert self.soldier.to_damage() == 0.3

    def test_get_damage(self):
        print("test_get_damage")
        self.soldier.health = 90
        self.soldier.get_damage(10.5)
        assert self.soldier.health == 79.5
        self.soldier.health = 40.5
        self.soldier.get_damage(3.4)
        assert self.soldier.health == 37.1
        self.soldier.health = -2.5
        self.soldier.get_damage(6.4)
        assert self.soldier.health == -2.5

    def test_incrs_experience(self):
        print("test_incrs_experience")
        self.soldier.experience = 44
        self.soldier.incrs_experience()
        assert self.soldier.experience == 44.01
        self.soldier.experience = 12.6
        self.soldier.incrs_experience()
        assert self.soldier.experience == 12.61
        self.soldier.experience = 50
        self.soldier.incrs_experience()
        assert self.soldier.experience == 50

    def test_new_unit(self):
        print("test_new_unit")
        assert isinstance(Soldier.new_unit(), Soldier)
