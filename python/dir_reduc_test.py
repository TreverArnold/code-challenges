from dir_reduc import dir_reduc


def test_dir_reduc():
    assert dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) == [
        "WEST"
    ]
    assert dir_reduc(["North", "East", "South", "West"]) == [
        "North",
        "East",
        "South",
        "West",
    ]
    assert dir_reduc(
        [
            "NORTH",
            "EAST",
            "NORTH",
            "EAST",
            "WEST",
            "WEST",
            "EAST",
            "EAST",
            "WEST",
            "SOUTH",
        ]
    ) == ["NORTH", "EAST"]
