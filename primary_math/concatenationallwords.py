from typing import List

"""
You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s that is a concatenation
of each word in words exactly once, in any order, and without any intervening characters.
"""


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []

        lookup = {}
        result = []

        for word in words:
            lookup[word] = lookup.get(word, 0)+1

        words_count = len(words)
        word_length = len(words[0])

        for i in range((len(s) - words_count * word_length) + 1):
            lookup_2 = {}
            for j in range(0, words_count):
                next_word_index = i + j * word_length
                word = s[next_word_index:next_word_index + word_length]

                if word not in lookup:
                    break

                lookup_2[word] = lookup_2.get(word, 0) + 1

                if lookup_2[word] > lookup[word]:
                    break

                if j + 1 == words_count:
                    result.append(i)

        return result


if __name__=='__main__':
    solute = Solution().findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"])
    print(solute)






