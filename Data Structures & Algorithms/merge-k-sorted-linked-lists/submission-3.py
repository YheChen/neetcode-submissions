# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        count = 0
        for head in lists:
            curr = head
            while curr:
                heapq.heappush(heap, (curr.val, count, curr))
                curr = curr.next
                count += 1
        dummy = ListNode(0)
        curr = dummy
        while heap:
            _, _, new = heapq.heappop(heap)
            curr.next = new
            curr = curr.next
        return dummy.next