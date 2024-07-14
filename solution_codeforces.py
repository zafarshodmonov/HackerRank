
class CodeForcesTest:
    
    @staticmethod
    def f4A_test() -> list[tuple]:
        return [
            (8, 'YES')
        ]

    @staticmethod   
    def f282A_test() -> list[tuple]:
        return [
            (['X++', '--X'], 0)
        ]
    
    pass
    

class CodeForces(CodeForcesTest):
    
    def f4A(self, n: int) -> str:
        if n == 2:
            return 'NO'
        return 'YES' if (n % 2 == 0) else 'NO'
    
    def f4A_p(self):

        # Input
        n = int(input())

        # Processing
        ans = self.f4A(n)

        # Output
        print(ans)

    def f282A(self, nums: list[str]) -> int:
        sana = 0
        for s in nums:
            if (s == '++X') or (s == 'X++'):
                sana += 1
            else:
                sana -= 1
        return sana
    
    def f282A_p(self):
        
        # Input
        def inp():
            rel = []
            n = int(input())
            for i in range(n):
                rel.append(input())
            return rel
        
        nums = inp()

        # Processing
        ans = self.f282A(nums)

        # Output
        print(ans)
    
    pass

    
codeforces = CodeForces()

def main() -> None:
    codeforces.f282A_p()


if __name__ == "__main__":
    main()
