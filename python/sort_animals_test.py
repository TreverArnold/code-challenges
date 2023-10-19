from sort_animals import sort_animals


class Animal:
    def __init__(self, name, number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs


def test_animals():
    animals = []
    assert sort_animals(animals) == []

    animals = [
        Animal("Cat", 4),
        Animal("Snake", 0),
        Animal("Dog", 4),
        Animal("Centipede", 50),
        Animal("Human", 2),
        Animal("Bird", 2),
        Animal("Cow", 4),
        Animal("Ant", 6),
    ]

    assert sort_animals(animals) == "Snake, Bird, Human, Cat, Cow, Dog, Ant, Centipede"
