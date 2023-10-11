import math
from warrior import Warrior


def test_init():
    my_warrior = Warrior()
    assert my_warrior.get_level() == 1
    assert my_warrior.get_rank() == "Pushover"
    assert my_warrior.get_experience() == 100
    assert my_warrior.get_achievements() == []


def test_train():
    my_warrior = Warrior()
    my_warrior.training(["Mowed the lawn", 1000, 1])
    assert my_warrior.get_experience() == 1100
    assert my_warrior.get_level() == 11
    assert my_warrior.get_rank() == "Novice"
    assert my_warrior.get_achievements() == ["Mowed the lawn"]


def test_update_rank_level():
    my_warrior = Warrior()
    my_warrior.experience = 10500
    my_warrior.update_rank_level()
    assert my_warrior.get_level() == 100
    assert my_warrior.get_rank() == "Greatest"


def test_battle():
    my_warrior = Warrior()
    my_warrior.experience = 4900
    my_warrior.level = 49
    my_warrior.rank = "Veteran"
    assert my_warrior.get_rank() == "Veteran"
    assert my_warrior.battle(52) == "An intense fight"
    assert my_warrior.get_experience() == 5080
    assert my_warrior.get_level() == math.floor(my_warrior.get_experience() / 100)
    assert my_warrior.get_rank() == "Sage"

    assert my_warrior.battle(90) == "You've been defeated"
    my_warrior.level = 67
    assert my_warrior.battle(70) == "An intense fight"
    my_warrior.level = 50
    assert my_warrior.battle(50) == "A good fight"
    my_warrior.level = 50
    assert my_warrior.battle(49) == "A good fight"
    my_warrior.level = 50
    assert my_warrior.battle(40) == "Easy fight"


def test_invalid_battle_level():
    my_warrior = Warrior()
    assert my_warrior.battle(0) == "Invalid level"
    assert my_warrior.battle(101) == "Invalid level"
