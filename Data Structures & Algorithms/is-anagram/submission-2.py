class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for char in s:
            if char not in d1:
                d1[char] = 1
            else:
                d1[char] += 1
        
        for char in t:
            if char not in d2:
                d2[char] = 1
            else:
                d2[char] += 1
        for key in d2:
            if key not in d1:
                return False

        for key in d1:
            if key not in d2:
                return False
            elif d1[key] != d2[key]:
                return False

        return True