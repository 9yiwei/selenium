import pytest


def add_two_num(a, b):
    return a + b


@pytest.mark.math
def test_small_num():
    assert add_two_num(1, 2) == 3, "The sum of 1 and 2 should be 3."


@pytest.mark.math
def test_large_num():
    assert add_two_num(100, 200) == 300, "The sum of 100 and 200 should be 300."