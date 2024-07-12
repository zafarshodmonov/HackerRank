
class ACMPTest:
    
    @staticmethod
    def f1_test() -> list[tuple]:
        return [
            (2, 3, 5)
        ]
    

class ACMP(ACMPTest):
    
    def f1(self, a: int, b: int) -> int:
        return a + b
    
    def f1_p(self):

        # Input
        a, b = map(int, input().split())

        # Processing
        ans = self.f1(a, b)

        # Output
        print(ans)

    
acmp = ACMP()

def main():
    acmp.f1_p()

if __name__ == "__main__":
    main()
    