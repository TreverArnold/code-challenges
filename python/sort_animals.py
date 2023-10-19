def sort_animals(animals):
    if not animals:
        return []
    sorted_animals = sorted(
        animals, key=lambda animal: (animal.number_of_legs, animal.name)
    )
    return ", ".join([animal.name for animal in sorted_animals])
