class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)

        return values[k - 1]