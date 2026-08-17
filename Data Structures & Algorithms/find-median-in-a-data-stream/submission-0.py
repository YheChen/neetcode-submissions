import heapq

class MedianFinder:

    def __init__(self):
        self.lower = []
        self.higher = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        heapq.heappush(self.higher, -heapq.heappop(self.lower))
        
        if len(self.lower) < len(self.higher):
            heapq.heappush(self.lower, -heapq.heappop(self.higher))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.higher):
            return -self.lower[0]
        return (-self.lower[0] + self.higher[0]) / 2.0
        