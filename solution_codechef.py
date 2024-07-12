
class CodeChefTest:

    @staticmethod
    def f1_test():
        return [
            ([1, 3, 7, 10], [10, 30, 70, 100])
        ]
    pass
    

class CodeChef(CodeChefTest):

    problemsID = {
        1: 'Fitness'
    }

    def f1(self, nums: list[int]) -> list[int]:
        return list(map(lambda x: 10 * x, nums))
    
    def f1_p(self):

        # Input
        def input_f1():
            T = int(input())
            rel = []
            for i in range(T):
                rel.append(int(input()))
            return rel
        
        nums = input_f1()

        # Processing
        ans = self.f1(nums)

        # Output
        def output_f1(nums: list[int]) -> None:
            for i in nums:
                print(i)
        
        output_f1(ans)

    pass
    

codechef = CodeChef()

def main():
    codechef.f1_p()

if __name__ == "__main__":
    main()
