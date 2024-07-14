import pytest

from solution_acmp import acmp
from solution_codechef import codechef
from solution_codeforces import codeforces
from solution_coderbyte import coderbyte
from solution_codewars import codewars
from solution_hackerrank import hackerrank
from solution_leetcode import leetcode
from solution_robocontest import robocontest


@pytest.mark.parametrize(
        "nums, out", # O'zgartirish mumkin!
        leetcode.f506_test()  # O'zgartirish mumkin!
)        
def test_test(nums, out):  # O'zgartirish mumkin!
    assert leetcode.f506(nums) == out  # O'zgartirish mumkin!
