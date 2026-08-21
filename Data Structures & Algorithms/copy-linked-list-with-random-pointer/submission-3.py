"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import deque

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        node_map = {head: Node(head.val)}
        q = deque([head])
        
        while q:
            curr = q.popleft()
            curr_cp = node_map[curr]
            if curr.next:
                if curr.next not in node_map:
                    node_map[curr.next] = Node(curr.next.val)
                curr_cp.next = node_map[curr.next]
                q.append(curr.next)
            if curr.random:
                if curr.random not in node_map:
                    node_map[curr.random] = Node(curr.random.val) if curr.random else None
                curr_cp.random = node_map[curr.random]

        return node_map[head]