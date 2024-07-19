
class CodeWarsTest:

    @staticmethod
    def f1_test():
        return [
            (False)
        ]
    
    def f1_test():
        return [
            ('GCAT', 'GCAU')
        ]

    pass
    

class CodeWars(CodeWarsTest):

    problemsID = {
        1: "Chuck Norris VII - True or False (Beginer)",
        2: "DNA to RNA Conversion"
    }

    def f1(self):
        return not True
    
    def f2(self, dna: str) -> str:
        return dna.replace('T', 'U')
    
    pass
    

codewars = CodeWars()
