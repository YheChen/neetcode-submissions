class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Need to find edge e = (u, v) where there exists path from u -> v
        # that doesnt use edge e in the path

        # DFS Helper Function
        def dfs(n):
            seen = set()
            def solve(n):
                if n == v:
                    return True
                if n in seen:
                    return False
                seen.add(n)
                for edge in edges:
                    if edge == curr_edge:
                        continue
                    if edge[0] == n:
                        if solve(edge[1]):
                            return True
                    if edge[1] == n:
                        if solve(edge[0]):
                            return True
                return False
            return solve(n)
        # We break ties by later appearance in edges, so iterate through edges
        # in reverse order
        for i in range(len(edges) - 1, -1, -1):
        # For each edge in edges, confirm endpoints u, v
            curr_edge = edges[i]
            u, v = curr_edge[0], curr_edge[1]
        # Use a graph search algorithm to see if we can find a path u -> v
        # Note that we cannot reuse the edge that originally connected u and v
        # This shouldn't be a problem because the problem explicitly states
        # The new edge wasn't already in the graph, so in our search we can
        # decide not to use said edge
            if dfs(u):
        # Return our edge
                return curr_edge