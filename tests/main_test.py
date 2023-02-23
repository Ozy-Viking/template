"""
main_test.py



Author: Zack Hankin
Started: 23/02/2023
"""
import pytest
import demo_precommit


def test_square_1():
    assert demo_precommit.square(1) == 1


def test_square_2():
    assert demo_precommit.square(2) == 4


def test_square_neg_2():
    assert demo_precommit.square(-2) == 4


if __name__ == "__main__":
    raise SystemExit(pytest.main(__file__))
