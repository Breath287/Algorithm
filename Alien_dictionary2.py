from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash_map = {}
        for index, letter in enumerate(order):
            hash_map[letter] = index

        for i in range(1, len(words)):
            flag = 0
            pre, cur = words[i-1], words[i]
            for j in range(min(len(pre), len(cur))):
                if hash_map[pre[j]] < hash_map[cur[j]]:
                    flag = 1
                    break
                elif hash_map[pre[j]] > hash_map[cur[j]]:
                    return False
            if not flag and len(pre) > len(cur):
                return False

        return True

