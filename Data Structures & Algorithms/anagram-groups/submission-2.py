class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for char in s:
                chars[(ord(char) - ord('a'))] += 1
            mapping[tuple(chars)].append(s)

        return list(mapping.values())