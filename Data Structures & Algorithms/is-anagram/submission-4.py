class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for char in s:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1
        for char in t:
            if char in count2:
                count2[char] += 1
            else:
                count2[char] = 1
        for key in count1:
            if key not in count2:
                return False
            if count1[key] != count2[key]:
                return False
        for key in count2:
            if key not in count1:
                return False
            if count1[key] != count2[key]:
                return False
        return True