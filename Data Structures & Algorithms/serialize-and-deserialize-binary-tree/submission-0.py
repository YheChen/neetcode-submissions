# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        output = []
        levels = []
        q = deque([root])
        while q:
            level = []
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)
            levels.append(level)
        # output = 1!2#3!N#N#4#5
        for level in levels:
            output.append('!')
            for val in level:
                if val:
                    output.append(str(val))
                else:
                    output.append('N')
                output.append('#')
            output.pop()
        output.pop(0)
        return ''.join(output)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        # ['1', '2#3', 'N#N#4#5']
        level_strs = data.split('!')
        # [['1'], ['2', '3'], ['N', 'N', '4', '5'], ['N', 'N', 'N', 'N']]
        levels_still_str = []
        for lvl in level_strs:
            levels_still_str.append(lvl.split('#'))
        levels = []
        for lvl in levels_still_str:
            level = []
            for val in lvl:
                if val == 'N':
                    level.append(None)
                else:
                    level.append(int(val))
            levels.append(level)
        # levels = [[1], [2, 3], [None, None, 4, 5], [None, None, None, None]]
        root = TreeNode(levels[0][0])
        n = len(levels)
        if n == 1:
            return root
        curr_level = 1
        q = deque([root])
        while q:
            level_size = len(q)
            children = levels[curr_level]
            for _ in range(level_size):
                node = q.popleft()
                left_child_val = children.pop(0)
                if not left_child_val:
                    node.left = None
                else:
                    left_child = TreeNode(left_child_val)
                    node.left = left_child
                    q.append(left_child)
                right_child_val = children.pop(0)
                if not right_child_val:
                    node.right = None
                else:
                    right_child = TreeNode(right_child_val)
                    node.right = right_child
                    q.append(right_child)

            curr_level += 1
        return root


        