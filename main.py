from random_testcase import RandomTestcase, random_testcase

from A_B import A, B
from input_output import Fin, Fout

from solution import hackerrank

r = RandomTestcase()

zafin = Fin()
zafout = Fout()

ans = random_testcase(100, r.solveMeFirst, hackerrank.solveMeFirst)

B('solveMeFirst', ans, (2, 1), zafin.solveMeFirst, zafout.solveMeFirst, 'R', 1)