
class CoderByteTest:

    @staticmethod
    def f1_test():
        return [
            ('fun&!! time', 'time')
        ]
    pass
    

class CoderByte(CoderByteTest):

    problemsID = {
        1: 'Longest Word'
    }
    
    def f1(self, s: str) -> str:

        def help_1(s: str) -> str:
            res = ""
            for ch in s:
                if ch.isalpha():
                    res += ch
            return res
        zamap = {}
        zamax = 0
        soz = ""
        for word in s.split():
            word = help_1(word)
            if len(word) > zamax:
                soz = word
                zamax = len(word)
        return soz
            
    pass
    

coderbyte = CoderByte()
