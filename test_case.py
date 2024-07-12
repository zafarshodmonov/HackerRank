import pytest

from solution_acmp import acmp
from solution_coderbyte import coderbyte
from solution_codechef import codechef
from solution_codeforces import codeforces
from solution_codewars import codewars
from solution_hackerrank import hackerrank
from solution_leetcode import leetcode
from solution_robocontest import robocontest


@pytest.mark.parametrize(
        "n, out", # O'zgartirish mumkin!
        codeforces.f4A_test()  # O'zgartirish mumkin!
)        
def test_test(n, out):  # O'zgartirish mumkin!
    assert codeforces.f4A(n) == out  # O'zgartirish mumkin!
