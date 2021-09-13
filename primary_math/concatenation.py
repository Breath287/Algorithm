from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic_map = {piece[0]: piece for piece in pieces}
        lst = []

        for item in arr:
            if item in dic_map:
                lst.extend(dic_map[item])

        return lst == arr


if __name__ == '__main__':
    s = Solution()
    print(s.canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))
