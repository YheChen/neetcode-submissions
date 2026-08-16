class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        seen = set()
        graph = {}
        for i in range(n):
            graph[i] = []
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(u, prev) -> bool:
            if u in seen:
                return False
            seen.add(u)
            for v in graph[u]:
                if v == prev:
                    continue
                if not dfs(v, u):
                    return False
            return True

        return dfs(0, -1) and len(seen) == n