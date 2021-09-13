# reverse a integer
class Solution:
    def reverse(self, x: int) -> int:
        ''' Max = 2^31 = 2147483648
            Min = -2^31 + 1 = 2147483648
        '''
        flag = 1
        if x == 0:
            return 0
        elif x < 0:
            flag = -1
            str_map = str(x)[1:]
        else:
            str_map = str(x)

        # reverse the str
        str_map = str_map[::-1]

        return int(str_map) * flag if x <= 2147483648 and x >= -2147483647 else None


if __name__ == '__main__':
    test = Solution().reverse(-7880)
    print(test)













