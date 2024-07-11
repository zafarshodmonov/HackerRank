import random


def random_testcase(number_of_testcase: int, fin, fout) -> list[tuple]:

    rel = []
    for i in range(number_of_testcase):
        zain = fin()
        
        m1 = type(zain) is tuple
        zaout = fout(* zain) if m1 else fout(zain)
        m2 = type(zaout) is tuple
        if m1 and m2:
            zatuple = (* zain, * zaout)
        elif m1 and not m2:
            zatuple = (* zain, zaout)
        elif not m1 and m2:
            zatuple = (zain, * zaout)
        else:
            zatuple = (zain, zaout)
        rel.append(zatuple)
    return rel

class RandomTestcase:

    @staticmethod
    def solveMeFirst():
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        return a, b
