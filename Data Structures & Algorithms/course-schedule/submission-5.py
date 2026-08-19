from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            indegree[prereq] += 1
            adj[course].append(prereq)
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return finish == numCourses