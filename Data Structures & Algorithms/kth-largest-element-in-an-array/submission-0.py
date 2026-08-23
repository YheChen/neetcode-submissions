class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        output = 0
        for _ in range(k):
            output = -heapq.heappop(heap)
        return output