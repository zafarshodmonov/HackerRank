
class CodeWarsTest:

    @staticmethod
    def f1_test():
        return [
            (False)
        ]

    pass
    

class CodeWars(CodeWarsTest):

    problemsID = {
        1: "Chuck Norris VII - True or False (Beginer)"
    }

    def f1(self):
        return not True
    
    pass
    

codewars = CodeWars()
