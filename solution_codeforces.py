
class CodeForcesTest:
    
    @staticmethod
    def f4A_test() -> list[tuple]:
        return [
            (8, 'YES')
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
    
    pass

    
codeforces = CodeForces()

def main() -> None:
    codeforces.f4A_p()


if __name__ == "__main__":
    main()
