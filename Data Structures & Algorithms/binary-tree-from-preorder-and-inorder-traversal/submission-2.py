# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def solve(l, r):
            nonlocal pre_idx
            if l > r:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            mid = inorder_idx[root_val]
            root.left = solve(l, mid - 1)
            root.right = solve(mid + 1, r)
            return root
        return solve(0, len(inorder) - 1)

