import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-num for num in nums]
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        temp = []
        for _ in range(self.k - 1):
            temp.append(heapq.heappop(self.heap))
        kth_largest = heapq.heappop(self.heap)
        temp.append(kth_largest)
        for _ in range(self.k):
            heapq.heappush(self.heap, temp.pop())
        return -kth_largest
