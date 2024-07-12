import pytest

from solution_acmp import acmp
from solution_codebyte import codebyte
from solution_codechef import codechef
from solution_codeforces import codeforces
from solution_codewars import codewars
from solution_hackerrank import hackerrank
from solution_leetcode import leetcode
from solution_robocontest import robocontest


@pytest.mark.parametrize(
        "nums, target, out", # O'zgartirish mumkin!
        leetcode.F1_test()  # O'zgartirish mumkin!
)        
def test_test(nums, target, out):  # O'zgartirish mumkin!
    assert leetcode.F1(nums, target) in out  # O'zgartirish mumkin!
    