import itertools


class Solution:
    def countArrangement(self, n: int) -> int:
        # generate permutations
        lst = [i+1 for i in range(n)]
        permutation = itertools.permutations(lst)
        count = 0
        # check beautiful range
        for ele in permutation:
            up = True
            for k, v in enumerate(ele):
                if v%(k+1) != 0 and (k+1)%v != 0:
                    up = False
            if up:
                count += 1
        return count


if __name__ == '__main__':
    a = Solution()
    print(a.countArrangement(5))













