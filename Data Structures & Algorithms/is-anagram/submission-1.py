class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            if not d.get(c):
                # t must not contain any new char
                return False
            d[c] += 1

        return all(map(lambda v: v % 2 == 0, d.values()))
