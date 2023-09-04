from bouncing_balls import bouncing_balls

def test_bounching_balls():
    assert bouncing_balls(2, 0.5, 3) == -1
    assert bouncing_balls(30, 0.75, 1.5) == 21
    assert bouncing_balls(3, 0.66, 1.5) == 3
    assert bouncing_balls(3, -0.66, 1.5) == -1
