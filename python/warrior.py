import math


class Warrior:
    def __init__(self):
        self.level = 1
        self.rank = "Pushover"
        self.experience = 100
        self.achievements = []

    def update_rank_level(self):
        if self.experience >= 10000:
            self.experience = 10000
            self.level = 100
        self.level = math.floor(self.experience / 100)
        if self.level > 9:
            self.rank = "Novice"
        if self.level > 19:
            self.rank = "Fighter"
        if self.level > 29:
            self.rank = "Warrior"
        if self.level > 39:
            self.rank = "Veteran"
        if self.level > 49:
            self.rank = "Sage"
        if self.level > 59:
            self.rank = "Elite"
        if self.level > 69:
            self.rank = "Conqueror"
        if self.level > 79:
            self.rank = "Champion"
        if self.level > 89:
            self.rank = "Master"
        if self.level > 99:
            self.rank = "Greatest"

    def get_level(self):
        return self.level

    def get_experience(self):
        return self.experience

    def get_rank(self):
        return self.rank

    def get_achievements(self):
        return self.achievements

    def training(self, training_info):
        if self.level >= training_info[2]:
            self.achievements.append(training_info[0])
            self.experience += training_info[1]
            self.update_rank_level()
            return training_info[0]
        return "Not strong enough"

    def battle(self, op_level):
        if op_level not in range(1, 101):
            return "Invalid level"
        elif op_level >= 5 + self.level and math.floor(op_level / 10) > math.floor(
            self.level / 10
        ):
            return "You've been defeated"
        elif op_level > self.level:
            self.experience += 20 * (op_level - self.level) * (op_level - self.level)
            self.update_rank_level()
            return "An intense fight"
        elif op_level == self.level:
            self.experience += 10
            self.update_rank_level()
            return "A good fight"
        elif op_level == self.level - 1:
            self.experience += 5
            self.update_rank_level()
            return "A good fight"
        elif op_level <= self.level - 2:
            return "Easy fight"
