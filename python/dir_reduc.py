def dir_reduc(arr):
    directions = []
    opposites = {
        "North": "South",
        "South": "North",
        "East": "West",
        "West": "East",
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST",
    }

    for direction in arr:
        if directions and directions[-1] == opposites.get(direction):
            directions.pop()
            dir_reduc(directions)
        else:
            directions.append(direction)

    if len(directions) < len(arr):
        return dir_reduc(directions)

    return directions
