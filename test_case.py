import pytest

from input_output import InputFunction, OutputFunction, Fin, Fout
from A_B import A, B
from solution import HackerRank

input_function = InputFunction()
output_function = OutputFunction()

fin = Fin()
fout = Fout()

ans = A("solveMeFirst", 2, input_function.solveMeFirst, output_function.solveMeFirst)
B("solveMeFirst", ans, (2, 1), fin.solveMeFirst, fout.solveMeFirst)

hackerrank = HackerRank()

@pytest.mark.parametrize(
        "a, b, out",
        ans
)
def test_hackerrank(a, b, out):
    assert hackerrank.solveMeFirst(a, b) == out