from readable_time import make_readable


def test_make_readable():
    assert make_readable(0) == "now"
    assert make_readable(1) == "1 second"
    assert make_readable(62) == "1 minute and 2 seconds"
    assert make_readable(120) == "2 minutes"
    assert make_readable(3600) == "1 hour"
    assert make_readable(3662) == "1 hour, 1 minute and 2 seconds"
    assert make_readable(7379854) == "85 days, 9 hours, 57 minutes and 34 seconds"
    assert make_readable(9699805) == "112 days, 6 hours, 23 minutes and 25 seconds"
