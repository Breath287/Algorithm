class Solution:
    def findLongest(self, s: str)->int:
        start = 0
        longest = 0
        dic_map = {}
        if len(s) == 0:
            return None
        if len(s) == 1:
            return 1
        for i, c in enumerate(s):
            if c in dic_map:
                start = max(start, dic_map[c] + 1)
            longest = max(longest, i - start + 1)
            dic_map[c] = i
        return longest

s = Solution().findLongest('abdajsdhhadjhda')
print(s)