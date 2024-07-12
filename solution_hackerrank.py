

class HackerRankTest:
    pass


class HackerRank(HackerRankTest):

    problemsID = {
        1: "https://www.hackerrank.com/challenges/arrays-ds/problem"
    }

    alphabet = [
        'A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J', 
        'K', 'L', 'M', 'N', 'O', 
        'P', 'Q', 'R', 'S', 'T', 
        'U', 'V', 'W', 'X', 'Y', 'Z']
    
    def F1(self, nums: list[int]) -> list[int]:
        n = len(nums)
        rel = []
        for i in range(n - 1, -1, -1):
            rel.append(nums[i])
        return rel


    def simpleArraySum(nums: list[int]) -> int:
        return sum(nums)
    
    def solveMeFirst(self, a: int, b: int) -> int:
        return a + b
    
    
hackerrank = HackerRank()
