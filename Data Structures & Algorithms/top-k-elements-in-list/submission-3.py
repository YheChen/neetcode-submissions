import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        heap = []
        heapq.heapify(heap)
        for num in freqs:
            heapq.heappush(heap, (-freqs[num], num))
        output = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            output.append(num)
        return output