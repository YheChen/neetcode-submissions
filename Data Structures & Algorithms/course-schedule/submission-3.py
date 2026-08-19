class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            pre_map[a].append(b)
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if not pre_map[course]:
                return True
            visited.add(course)
            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            pre_map[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
        
