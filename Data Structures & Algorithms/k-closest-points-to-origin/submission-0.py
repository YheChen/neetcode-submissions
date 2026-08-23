import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y) -> int:
            return math.sqrt(x * x + y * y)
        
        heap = []

        for point in points:
            heapq.heappush(heap, (dist(point[0], point[1]), point))
        
        output = []
        for _ in range(k):
            _, point = heapq.heappop(heap)
            output.append(point)
        return output