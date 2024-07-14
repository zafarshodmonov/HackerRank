import heapq


class LeetCodeTest:

    @staticmethod
    def F1_test():
        return [
            ([2, 7, 11, 15], 9, [[0, 1]]),
            ([3, 2, 4], 6, [[0, 0], [1, 2]]),
            ([3, 3], 6, [[0, 0], [0, 1], [1, 1]]),
            ([1, 2, 3, 4, 5, 6], 5, [[0, 3], [1, 2]]),
            ([1, 7, 8, 3, 5], 9, [[0, 2], [3, 4]])
        ]
    
    @staticmethod
    def F20_test():
        return [
            ('()', True),
            ('()[]{}', True),
            ('(]', False),
            ('(', False),
            (']', False)
        ]

    @staticmethod
    def F326_test():
        return [
            (27, True),
            (0, False),
            (-1, False)
        ]

    @staticmethod
    def F412_test():
        return [
            (3, ["1","2","Fizz"]),
            (5, ["1","2","Fizz","4","Buzz"]),
            (15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])
        ]
    
    @staticmethod
    def f506_test() -> list[tuple]:
        return [
            ([5,4,3,2,1], ["Gold Medal","Silver Medal","Bronze Medal","4","5"])
        ]

    @staticmethod
    def F509_test():
        return [
            (6, 8),
            (0, 0),
            (1, 1),
            (20, 6765),
            (30, 832040)
        ]


class LeetCode(LeetCodeTest):

    def F1(self, nums: list[int], target: int) -> list[int]:
        m = {}
        for i, e in enumerate(nums):
            if e in m:
                return [m[e], i]
            
            m[target - e] = i

    def F20(self, s: str) -> bool:

        zamap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for l in s:
            if l in zamap:
                if stack == []:
                    return False
                if zamap[l] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        return True if stack == [] else False

    def F21(self, l1, l2):

        def help_1(l1, l2, t):
            if l1 is None and l2 is None:
                return
            elif l1 is None and l2:
                t.next = l2
                return 
            elif l1 and l2 is None:
                return
            else:
                a = l1.val
                b = l2.val
                if a == b:
                    l1_next = l1.next
                    l2_next = l2.next
                    t = l2
                    l1.next = l2
                    l2.next = l1_next
                    help_1(l1_next, l2_next, t)
                elif a > b:
                    l1_next = l1.next
                    l2_next = l2.next
                    l1.next = l2
                    l2.next = l1_next
                    l1.val = b
                    l2.val = a
                    t = l1
                    help_1(l2, l2_next, t)
                else:
                    t = l1
                    l1 = l1.next
                    help_1(l1, l2, t)

        head = l1
        if not l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        else:
            help_1(l1, l2, l1)
        return head
    
    def F88(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        if m and n:
            for i in range(m, m + n):
                nums1[i] = None
            i = 0
            j = 0
            temp = None
            for _ in range(m + n):
                item1 = nums1[i]
                if temp is None:
                    item2 = nums2[j]
                else:
                    item2 = temp
                if item1 is None:
                    nums1[i] = item2
                    i += 1
                    j += 1
                else:
                    if item1 <= item2:
                        if temp is None:
                            nums1[i]
                        i += 1
                    else:
                        temp = item1
                        nums1[i] = nums2[j]
                        i += 1
            return 
        elif not m and n:
            for i, e in enumerate(nums2):
                nums1[i] = e
            return
        elif m and not n:
            return
        else:
            return

    def F326(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 0:
            return False
        asos = n // 3
        qoldiq = n % 3
        if qoldiq != 0 or asos == 0:
            return False
        else:
            return self.F326(asos)
        
    def F326_idea1(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            asos = n // 3
            qoldiq = n % 3
            if qoldiq != 0:
                return False
            n = asos
        return True
            
    def F412(self, n: int) -> list[str]:

        def help_1():
            return "FizzBuzz"

        def help_2():
            return "Fizz"
        
        def help_3():
            return "Buzz"

        def help_4(self, n: int) -> str:
            return str(n)

        rel = []
        for i in range(1, n + 1):
            a = i % 3 == 0
            b = i % 5 == 0
            if a and b:
                rel.append(help_1())
            elif a:
                rel.append(help_2())
            elif b:
                rel.append(help_3())
            else:
                rel.append(help_4(i))
        return rel 
    
    def f506(self, nums: list[int]) -> list[str]:

        N = len(score)

        # Create a heap of pairs (score, index)
        heap = []
        for index, score in enumerate(score):
            heapq.heappush(heap, (-score, index))
        
        # Assign ranks to athletes
        rank = [0] * N
        place = 1
        while heap:
            original_index = heapq.heappop(heap)[1]
            if place == 1:
                rank[original_index] = "Gold Medal"
            elif place == 2:
                rank[original_index] = "Silver Medal"
            elif place == 3:
                rank[original_index] = "Bronze Medal"
            else:
                rank[original_index] = str(place)
            place +=1
            
        return rank


    def F509(self, n: int) -> int:
        if n < 2:
            return n
        else:
            return self.F509(n - 1) + self.F509(n - 2)


leetcode = LeetCode()