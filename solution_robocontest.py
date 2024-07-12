
class RoboContestTest:

    @staticmethod
    def f1_test():
        return [
            (2, 3, 5)
        ]

    pass
    

class RoboContest(RoboContestTest):
    
    def f1(self, a: int, b: int) -> int:
        return a + b

    def f1_p(self):
        
        # Input
        a, b = map(int, input().split())

        # Processing
        ans = self.f1(a, b)

        # Output
        print(ans)
    pass
    
robocontest = RoboContest()

def main():
    robocontest.f1_p()

if __name__ == "__main__":
    main()
