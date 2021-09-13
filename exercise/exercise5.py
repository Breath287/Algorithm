# given a string, find the longest palindromic
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = s[0]

        # travel the string, find even palindromic, then return longest one
        for i in range(1, n):
            right = i
            left = right - 1
            while right < n and left >= 0 and s[right] == s[left]:
                right += 1
                left -= 1
            res = max(res, s[left+1:right], key=lambda x: len(x))

            # find the odd palindromic
            left = i - 1
            right = i + 1
            while right < n and left >= 0 and s[left] == s[right]:
                right += 1
                left -= 1
            res = max(res, s[left+1:right], key=lambda x: len(x))
        return res


if __name__ == '__main__':
    a = Solution().longestPalindrome('abcdcbaeds')
    print(a)
