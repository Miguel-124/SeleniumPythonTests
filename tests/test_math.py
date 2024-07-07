import pytest
def add_two(a, b):
    return a+b

@pytest.mark.math
def test_add_two_small_numbers():
    assert add_two(1, 2) == 3, "1+2 should be 3"
@pytest.mark.math
def test_add_two_large_numbers():
    assert add_two(1000123, 2123000) == 3123123, "1000123+2123000 should be 3123123"