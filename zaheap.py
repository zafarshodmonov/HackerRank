import heapq


def heapify_up(nums: list[int], index: int, heap_type: str = 'min') -> list[int]:

    def parent_index(index: int) -> int:
        return (index - 1) // 2
    
    if heap_type == "min":
        while (index > 0) and (nums[index] < nums[parent_index(index)]):
            nums[index], nums[parent_index(index)] = nums[parent_index(index)], nums[index]
            index = parent_index(index)
    else:
        while (index > 0) and (nums[index] > nums[parent_index(index)]):
            nums[index], nums[parent_index(index)] = nums[parent_index(index)], nums[index]
            index = parent_index(index)

def heapify_down(nums, n, i, heap_type):
    """
    1. Summary Line:
        This function ensures that the subtree rooted at index 'i' follows the heap property.

    2. Description:
        * This function ensures that the subtree rooted at index 'i' follows the heap property.
        * Depending on whether 'heap_type' is 'min' or 'max', it adjusts the tree to maintain 
        either the min-heap or max-heap property.
        * It compares the root with its children and swaps them if necessary, then 
        recursively heapifies the affected subtree.

    3. Parameters:
        nums (list[int]): Represents an unsorted array.
        n (int): Represents the length of the 'nums' array.
        i (int): Ajdkfjkdjflkjdklfjdkjkdjkfjdkjfkdjkdjkfjd.
        heap_type (str): 
            Depending on whether 'heap_type' is 'min' or 'max', it adjusts the tree to maintain 
            either the min-heap or max-heap property.

    4. Returns:
        list[int]: Represents 'Min-Heaps' or 'Max-Heaps' in array form.

    5. Raises:
        ValueError: Ajlkjfkljkfjkjkjkjkfjdkljdhfjghjfhdjhfjhjdhfj.

    6. Examples:
        >>> heapify([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 11, 4, 'min')
        [3, 1, 4, 1, 3, 9, 2, 6, 5, 5, 5]

    """

    largest_or_smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if heap_type == 'min':
        if left < n and nums[left] < nums[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and nums[right] < nums[largest_or_smallest]:
            largest_or_smallest = right
    else: # 'max'
        if left < n and nums[left] > nums[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and nums[right] > nums[largest_or_smallest]:
            largest_or_smallest = right

    if largest_or_smallest != i:
        nums[i], nums[largest_or_smallest] = nums[largest_or_smallest], nums[i]
        heapify_down(nums, n, largest_or_smallest, heap_type)

def build_heap(nums, heap_type='min'):
    """
    1. Summary Line:
        This function transforms the array nums into a heap.

    2. Description:
        * This function transforms the array nums into a heap.
        * It starts from the last non-leaf node and applies heapify to all nodes in reverse level 
        order to ensure the entire array satisfies the heap property.
        * The default heap_type is 'min', but it can be set to 'max' to build a max-heap instead.

    3. Parameters:
        nums (list[int]): Represents an unsorted array.
        heap_type (str): 
            Depending on whether 'heap_type' is 'min' or 'max', it adjusts the tree to maintain 
            either the min-heap or max-heap property.

    4. Returns:
        list[int]: Represents 'Min-Heaps' or 'Max-Heaps' in array form.

    5. Raises:
        ValueError: Ajlkjfkljkfjkjkjkjkfjdkljdhfjghjfhdjhfjhjdhfj.

    6. Examples:
        >>> build_heap([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 'min')
        [1, 1, 2, 3, 3, 9, 4, 6, 5, 5, 5]
        >>> build_heap([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 'max')
        [9, 6, 4, 5, 5, 3, 2, 1, 1, 3, 5]

    """
    
    def heapify(nums, n, i, heap_type):
        """
        1. Summary Line:
            This function ensures that the subtree rooted at index 'i' follows the heap property.

        2. Description:
            * This function ensures that the subtree rooted at index 'i' follows the heap property.
            * Depending on whether 'heap_type' is 'min' or 'max', it adjusts the tree to maintain 
            either the min-heap or max-heap property.
            * It compares the root with its children and swaps them if necessary, then 
            recursively heapifies the affected subtree.

        3. Parameters:
            nums (list[int]): Represents an unsorted array.
            n (int): Represents the length of the 'nums' array.
            i (int): Ajdkfjkdjflkjdklfjdkjkdjkfjdkjfkdjkdjkfjd.
            heap_type (str): 
                Depending on whether 'heap_type' is 'min' or 'max', it adjusts the tree to maintain 
                either the min-heap or max-heap property.

        4. Returns:
            list[int]: Represents 'Min-Heaps' or 'Max-Heaps' in array form.

        5. Raises:
            ValueError: Ajlkjfkljkfjkjkjkjkfjdkljdhfjghjfhdjhfjhjdhfj.

        6. Examples:
            >>> heapify([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 11, 4, 'min')
            [3, 1, 4, 1, 3, 9, 2, 6, 5, 5, 5]

        """

        largest_or_smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if heap_type == 'min':
            if left < n and nums[left] < nums[largest_or_smallest]:
                largest_or_smallest = left
            if right < n and nums[right] < nums[largest_or_smallest]:
                largest_or_smallest = right
        else: # 'max'
            if left < n and nums[left] > nums[largest_or_smallest]:
                largest_or_smallest = left
            if right < n and nums[right] > nums[largest_or_smallest]:
                largest_or_smallest = right

        if largest_or_smallest != i:
            nums[i], nums[largest_or_smallest] = nums[largest_or_smallest], nums[i]
            heapify(nums, n, largest_or_smallest, heap_type)

    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i, heap_type)
    return nums

def insert(nums: list[int], key: int):
    nums.append(key)
    heapify_up(nums, len(nums) - 1)
    return nums

def extract_min(nums, heap_type: str = 'min'):
    if len(nums) == 0:
        raise IndexError("Heap is empty")
    min_element = nums[0]
    nums[0] = nums.pop()
    heapify_down(nums, len(nums), 0, heap_type)
    return min_element

def peek(nums):
    if len(nums) == 0:
        raise IndexError("Heap is empty")
    return nums[0]


class MinHeap:

    def __init__(self):
        self.heap = []
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self._parent(index)]:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)
    
    def _heapify_down(self, index):
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
    
    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_element
    
    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]


# # Example usage
# min_heap = MinHeap()
# min_heap.insert(3)
# min_heap.insert(2)
# min_heap.insert(1)

# print(min_heap.extract_min())  # Outputs: 1
# print(min_heap.peek())         # Outputs: 2

def main() -> None:

    nums = [1, 3, 2, 4]
    # max_heap_1 = build_heap(nums.copy(), 'max')
    # print(max_heap_1)

    h = []
    for i in nums:
        heapq.heappush(h, -i)
    
    h = [-i for i in h]
    print(h)

    pass


if __name__ == "__main__":
    main()
