from vowel_count_code import vowel_count


def test_vowel_count():
    assert vowel_count("hdsfbaeacik") == 4
    assert vowel_count("sdfnobvjna") == 2
