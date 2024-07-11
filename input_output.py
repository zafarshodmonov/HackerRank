
     
class InputFunction:

    def solveMeFirst(self, inputs: list[str]):
        a = int(inputs[0])
        b = int(inputs[1])
        return a, b

   
class OutputFunction:

    def solveMeFirst(self, outputs: list[str]) -> int:
        n = int(outputs[0])
        return n


class Fin:
    
    def solveMeFirst(self, zatuple: tuple):
        
        res = ''
        for i in zatuple:
            res += "{}{}".format(i, "\n")
        res = res[:-1]
        return res


class Fout:
    
    def solveMeFirst(self, zatuple: tuple):
        
        res = ''
        for i in zatuple:
            res += "{}{}".format(i, "\n")
        res = res[:-1]
        return res
    pass