class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = {'(': ')', '{': '}', '[':']'}
        right = {')': '(', '}': '{', ']':'['}
        for char in s:
            if char in left:
                stack.append(char)
            elif char in right:
                if not stack:
                    return False
                top = stack.pop()
                if top != right[char]:
                    return False
        return True if not stack else False