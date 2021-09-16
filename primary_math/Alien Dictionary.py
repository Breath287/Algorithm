from typing import List


"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien language.
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lookup_map = {}
        # create hashmap of order
        for index, letter in enumerate(order):
            lookup_map[letter] = index

        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return False
            for letter1, letter2 in zip(word1, word2):
                if lookup_map[letter1] > lookup_map[letter2]:
                    return False
                elif lookup_map[letter1] < lookup_map[letter2]:
                    break

        return True

