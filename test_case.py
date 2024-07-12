import pytest

from solution import HackerRank

hackerrank = HackerRank()

@pytest.mark.parametrize(
        "a, b, out",
        [
            (2, 3, 5)
        ]
)
def test_hackerrank(a, b, out):
    assert hackerrank.solveMeFirst(a, b) == out