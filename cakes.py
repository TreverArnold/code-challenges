def cakes(recipe, available):
    max_cakes = float('inf')
    for ingredient, quantity in recipe.items():
        if ingredient not in available:
            return 0
        max_cakes = min(max_cakes, available[ingredient] // quantity)
    return max_cakes